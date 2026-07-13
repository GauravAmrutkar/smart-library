from django.db import models


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