"""
Inventory module constants.
"""

from django.db import models

# ==========================================================
# Library Branch
# ==========================================================


class BranchStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"


# ==========================================================
# Book Copy
# ==========================================================


class BookCopyStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Available"
    BORROWED = "BORROWED", "Borrowed"
    RESERVED = "RESERVED", "Reserved"
    MAINTENANCE = "MAINTENANCE", "Maintenance"
    LOST = "LOST", "Lost"
    DAMAGED = "DAMAGED", "Damaged"
    DISCARDED = "DISCARDED", "Discarded"


class BookCondition(models.TextChoices):
    NEW = "NEW", "New"
    GOOD = "GOOD", "Good"
    FAIR = "FAIR", "Fair"
    POOR = "POOR", "Poor"
