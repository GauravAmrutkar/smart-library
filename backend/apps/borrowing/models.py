from django.conf import settings
from django.db import models

from apps.books.models import Book
from apps.inventory.models import BookCopy


class BorrowTransaction(models.Model):
    class Status(models.TextChoices):
        BORROWED = "BORROWED", "Borrowed"
        RETURNED = "RETURNED", "Returned"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="borrow_transactions",
    )

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="borrow_transactions"
    )
    book_copy = models.ForeignKey(
        BookCopy,
        on_delete=models.PROTECT,
        related_name="borrow_transactions",
        null=True,
        blank=True,
    )

    borrow_date = models.DateField(auto_now_add=True)

    due_date = models.DateField()

    return_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.BORROWED
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
