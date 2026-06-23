from datetime import timedelta

from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.books.models import Book
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

        book = Book.objects.get(id=book_id)

        inventory = book.inventory

        if inventory.available_library_stock <= 0:
            raise ValidationError("Book unavailable.")

        inventory.available_library_stock -= 1

        inventory.save()

        due_date = timezone.now().date() + timedelta(days=15)

        transaction = BorrowTransaction.objects.create(
            user=user, book=book, due_date=due_date
        )

        return transaction
