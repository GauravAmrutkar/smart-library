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
    def available_copies(book):

        return BookCopy.objects.filter(
            book=book,
            status=BookCopyStatus.AVAILABLE,
        ).select_related(
            "shelf",
            "shelf__rack",
            "shelf__rack__floor",
            "shelf__rack__floor__branch",
        )