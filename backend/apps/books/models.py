from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(
        max_length=255
    )

    bio = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=255
    )

    isbn = models.CharField(
        max_length=20,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    publication_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title