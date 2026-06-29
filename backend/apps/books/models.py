from django.db import models
from django.db.models import Q

from .constants import BookStatus, CoverType

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """
    Stores book publisher information.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Language(models.Model):
    """
    Represents the language in which a book is published.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=10,
        unique=True,
        help_text="ISO language code. Example: en, hi, mr",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.code})"


class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(
        max_length=255,
        blank=True,
    )

    isbn_13 = models.CharField(
        max_length=20,
        unique=True,
    )

    isbn_10 = models.CharField(
        max_length=15,
        blank=True,
    )

    description = models.TextField(blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="books"
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )
    edition = models.CharField(
        max_length=100,
        blank=True,
    )

    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_type = models.CharField(
        max_length=20,
        choices=CoverType.choices,
        default=CoverType.PAPERBACK,
    )

    status = models.CharField(
        max_length=20,
        choices=BookStatus.choices,
        default=BookStatus.ACTIVE,
    )

    publication_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookImage(models.Model):
    """
    Stores one or more images associated with a book.
    """

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="books/",
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
    )

    is_primary = models.BooleanField(
        default=False,
        help_text="Primary cover image displayed in listings.",
    )

    display_order = models.PositiveIntegerField(
        default=1,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "display_order",
            "id",
        ]

    def __str__(self):
        return f"{self.book.title} - Image {self.id}"


class Inventory(models.Model):
    book = models.OneToOneField(
        Book, on_delete=models.CASCADE, related_name="inventory"
    )

    library_stock = models.PositiveIntegerField(default=0)

    available_library_stock = models.PositiveIntegerField(default=0)

    store_stock = models.PositiveIntegerField(default=0)

    available_store_stock = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(available_library_stock__gte=0),
                name="library_stock_non_negative",
            ),
            models.CheckConstraint(
                condition=Q(available_store_stock__gte=0),
                name="store_stock_non_negative",
            ),
        ]

    def __str__(self):
        return self.book.title
