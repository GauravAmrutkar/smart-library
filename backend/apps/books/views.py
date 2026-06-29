from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.exceptions import ValidationError
from rest_framework import generics
from apps.users.permissions import IsAdminUserRole

from .models import Publisher, Book, Inventory
from .serializers import PublisherSerializer, BookSerializer, InventorySerializer
from .service import PublisherService
from django_filters.rest_framework import DjangoFilterBackend
from .validators import PublisherValidator


class BookListView(generics.ListAPIView):
    queryset = Book.objects.select_related("author", "category").all()

    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "author",
        "category",
    ]


class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.select_related("book")

    serializer_class = InventorySerializer


class InventoryCreateView(generics.CreateAPIView):
    serializer_class = InventorySerializer

    permission_classes = [IsAuthenticated, IsAdminUserRole]


class InventoryUpdateView(generics.UpdateAPIView):
    queryset = Inventory.objects.all()

    serializer_class = InventorySerializer

    permission_classes = [IsAuthenticated, IsAdminUserRole]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by("name")

    serializer_class = PublisherSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def perform_create(self, serializer):

        PublisherValidator.validate_unique_name(serializer.validated_data["name"])

        serializer.save()

    def perform_destroy(self, instance):

        if not PublisherService.can_delete(instance):
            raise ValidationError("Cannot delete a publisher with associated books.")

        instance.delete()
