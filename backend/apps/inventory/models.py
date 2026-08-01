from django.db import models, transaction
from django.db.models import Max
from decimal import Decimal

from apps.books.models import Book

from .constants import (
    BranchStatus,
    BookCopyStatus,
    BookCondition,
)

class LibraryBranch(models.Model):
    """
    Represents a physical library branch.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    code = models.CharField(
        max_length=20,
        unique=True,
        help_text="Unique branch code. Example: PUN001",
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    postal_code = models.CharField(
        max_length=20,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Library Branch"
        verbose_name_plural = "Library Branches"

    def __str__(self):
        return f"{self.name} ({self.code})"


class Floor(models.Model):
    """
    Represents a floor within a library branch.
    """

    branch = models.ForeignKey(
        LibraryBranch,
        on_delete=models.CASCADE,
        related_name="floors",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["branch", "name"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "branch",
                    "code",
                ],
                name="unique_floor_code_per_branch",
            )
        ]

    def __str__(self):
        return f"{self.branch.code} - {self.name}"


class Rack(models.Model):
    """
    Represents a rack inside a library branch.
    """

    branch = models.ForeignKey(
        LibraryBranch,
        on_delete=models.CASCADE,
        related_name="racks",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["branch", "name"]

        constraints = [
            models.UniqueConstraint(
                fields=["branch", "code"],
                name="unique_rack_code_per_branch",
            )
        ]

    def __str__(self):
        return f"{self.branch.code} - {self.code}"


class Shelf(models.Model):
    """
    Represents a shelf inside a rack.
    """

    rack = models.ForeignKey(
        Rack,
        on_delete=models.CASCADE,
        related_name="shelves",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    description = models.TextField(
        blank=True,
    )

    capacity = models.PositiveIntegerField(
        default=100,
        help_text="Maximum number of book copies this shelf can hold.",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["rack", "name"]

        constraints = [
            models.UniqueConstraint(
                fields=["rack", "code"],
                name="unique_shelf_code_per_rack",
            )
        ]

    def __str__(self):
        return f"{self.rack.code} - {self.code}"




class BookCopy(models.Model):
    """
    Represents a single physical copy of a book.
    """

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="copies",
    )

    shelf = models.ForeignKey(
        Shelf,
        on_delete=models.PROTECT,
        related_name="book_copies",
    )

    accession_number = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
    )

    barcode = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=BookCopyStatus.choices,
        default=BookCopyStatus.AVAILABLE,
    )

    condition = models.CharField(
        max_length=20,
        choices=BookCondition.choices,
        default=BookCondition.NEW,
    )

    purchase_date = models.DateField(
        null=True,
        blank=True,
    )

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    supplier = models.CharField(
        max_length=255,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "accession_number",
        ]

    def __str__(self):
        return f"{self.accession_number} - {self.book.title}"

    def save(self, *args, **kwargs):

        if not self.accession_number:

            self.accession_number = self.generate_accession_number()

        if not self.barcode:

            self.barcode = self.accession_number

        super().save(*args, **kwargs)

    @classmethod
    def generate_accession_number(cls):

        with transaction.atomic():

            last_copy = (
                cls.objects.select_for_update()
                .order_by("-id")
                .first()
            )

            if not last_copy:

                return "LIB000001"

            last_number = int(
                last_copy.accession_number.replace(
                    "LIB",
                    "",
                )
            )

            return f"LIB{last_number + 1:06d}"
        
