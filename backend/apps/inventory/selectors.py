from .constants import BookCopyStatus
from .models import BookCopy, Rack, Shelf


class RackSelector:
    @staticmethod
    def get_active_racks():
        return Rack.objects.filter(is_active=True).select_related("branch")


class ShelfSelector:
    @staticmethod
    def get_active_shelves():
        return Shelf.objects.filter(is_active=True).select_related(
            "rack",
            "rack__floor",
            "rack__floor__branch",
        )


class BookCopySelector:
    @staticmethod
    def get_available_copy(book):

        return (
            BookCopy.objects.select_for_update()
            .select_related(
                "book",
                "shelf",
                "shelf__rack",
                "shelf__rack__floor",
                "shelf__rack__floor__branch",
            )
            .filter(
                book=book,
                status=BookCopyStatus.AVAILABLE,
            )
            .order_by("accession_number")
            .first()
        )
