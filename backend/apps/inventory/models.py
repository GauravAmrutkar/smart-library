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
