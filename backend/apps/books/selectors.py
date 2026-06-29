from .models import Publisher


class PublisherSelector:
    """
    Database queries related to publishers.
    """

    @staticmethod
    def list_publishers():
        return Publisher.objects.all()

    @staticmethod
    def get_publisher(pk):
        return Publisher.objects.get(pk=pk)
