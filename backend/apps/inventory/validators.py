from rest_framework.exceptions import ValidationError

from .models import Rack, Shelf


class RackValidator:
    @staticmethod
    def validate_unique_code(branch, code):

        if Rack.objects.filter(
            branch=branch,
            code__iexact=code,
        ).exists():
            raise ValidationError({"code": "Rack code already exists in this branch."})


class ShelfValidator:
    @staticmethod
    def validate_unique_code(rack, code):

        if Shelf.objects.filter(
            rack=rack,
            code__iexact=code,
        ).exists():
            raise ValidationError({"code": "Shelf code already exists in this rack."})

class BookCopyValidator:

    @staticmethod
    def validate_shelf_capacity(shelf):

        current = shelf.book_copies.count()

        if current >= shelf.capacity:

            raise ValidationError(
                {
                    "shelf":
                    "Shelf capacity exceeded."
                }
            )