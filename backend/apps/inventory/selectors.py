from .models import Rack, Shelf


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
