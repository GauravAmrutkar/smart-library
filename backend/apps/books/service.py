from .models import Publisher


class PublisherService:
    """
    Business workflows for Publisher.
    """

    @staticmethod
    def can_delete(publisher):
        """
        Business rule:
        A publisher cannot be deleted if books reference it.
        """
        return not publisher.books.exists()
