from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.books.models import Book
from apps.inventory.selectors import BookCopySelector
from apps.subscriptions.models import UserSubscription

from .models import BorrowTransaction


class BorrowService:
    @staticmethod
    @transaction.atomic
    def borrow_book(user, book_id):

        subscription = (
            UserSubscription.objects.select_related("plan")
            .filter(
                user=user,
                status="ACTIVE",
            )
            .first()
        )

        if not subscription:
            raise ValidationError("No active subscription.")

        active_books = BorrowTransaction.objects.filter(
            user=user,
            status="BORROWED",
        ).count()

        if active_books >= subscription.plan.max_active_books:
            raise ValidationError("Borrow limit reached.")

        book = Book.objects.get(id=book_id)

        copy = BookCopySelector.get_available_copy(book)

        if not copy:
            raise ValidationError("No copy available.")

        copy.mark_as_borrowed()

        transaction = BorrowTransaction.objects.create(
            user=user,
            book=book,  # Keep for now
            book_copy=copy,  # New field
            status="BORROWED",
        )

        return transaction


class ReturnService:
    @staticmethod
    def return_book(
        user,
        transaction_id,
    ):

        with transaction.atomic():
            transaction_obj = (
                BorrowTransaction.objects.select_for_update()
                .select_related("book")
                .filter(
                    id=transaction_id,
                    user=user,
                )
                .first()
            )

            if not transaction_obj:
                raise ValidationError("Transaction not found.")

            if transaction_obj.status == BorrowTransaction.Status.RETURNED:
                raise ValidationError("Book already returned.")

            borrow = BorrowTransaction.objects.get(
                id=transaction_id,
            )

            borrow.status = "RETURNED"

            borrow.return_date = timezone.now()

            borrow.save()

            borrow.book_copy.mark_as_available()

            transaction_obj.status = BorrowTransaction.Status.RETURNED

            transaction_obj.return_date = timezone.now().date()

            transaction_obj.save()
            active_books = BorrowTransaction.objects.filter(
                user=user, status=BorrowTransaction.Status.BORROWED
            ).count()
            active_books = BorrowTransaction.objects.filter(
                user=user, status=BorrowTransaction.Status.BORROWED
            ).count()
            subscription = UserSubscription.objects.filter(
                user=user, status=UserSubscription.Status.ACTIVE
            ).first()
            if subscription and active_books == 0:
                subscription.status = UserSubscription.Status.PAUSED

                subscription.save(update_fields=["status"])

        return transaction_obj
