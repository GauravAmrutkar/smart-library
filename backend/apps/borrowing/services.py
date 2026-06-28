from datetime import timedelta

from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.books.models import Book, Inventory
from apps.subscriptions.models import UserSubscription

from .models import BorrowTransaction


class BorrowService:
    @staticmethod
    def borrow_book(user, book_id):

        subscription = (
            UserSubscription.objects.filter(user=user, status="ACTIVE")
            .select_related("plan")
            .first()
        )

        if not subscription:
            raise ValidationError("No active subscription found.")

        active_books = BorrowTransaction.objects.filter(
            user=user, status="BORROWED"
        ).count()

        if active_books >= subscription.plan.max_active_books:
            raise ValidationError("Borrow limit reached.")

        with transaction.atomic():
            book = Book.objects.select_related("inventory").get(id=book_id)

            inventory = Inventory.objects.select_for_update().get(book=book)

            if inventory.available_library_stock <= 0:
                raise ValidationError("Book unavailable.")

            inventory.available_library_stock -= 1

            inventory.save()

            due_date = timezone.now().date() + timedelta(days=15)

            transaction_obj = BorrowTransaction.objects.create(
                user=user,
                book=book,
                due_date=due_date,
            )
            subscription.status = UserSubscription.Status.ACTIVE

            subscription.save(update_fields=["status"])
        return transaction_obj


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

            inventory = Inventory.objects.select_for_update().get(
                book=transaction_obj.book
            )

            inventory.available_library_stock += 1

            inventory.save()

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
