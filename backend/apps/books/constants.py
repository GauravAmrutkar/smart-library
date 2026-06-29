from django.db import models


class BookStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    DISCONTINUED = "DISCONTINUED", "Discontinued"


class CoverType(models.TextChoices):
    PAPERBACK = "PAPERBACK", "Paperback"
    HARDCOVER = "HARDCOVER", "Hardcover"
    EBOOK = "EBOOK", "eBook"
    AUDIOBOOK = "AUDIOBOOK", "Audiobook"
