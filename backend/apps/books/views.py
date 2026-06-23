from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.permissions import IsAdminUserRole

from .models import Book, Inventory
from .serializers import BookSerializer, InventorySerializer


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
