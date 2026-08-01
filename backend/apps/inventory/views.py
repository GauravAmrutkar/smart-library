from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.permissions import IsAdminUserRole

from .models import LibraryBranch, Rack, Shelf
from .serializers import LibraryBranchSerializer, RackSerializer, ShelfSerializer


class LibraryBranchViewSet(viewsets.ModelViewSet):
    queryset = LibraryBranch.objects.all()

    serializer_class = LibraryBranchSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]


class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.select_related("branch")

    serializer_class = RackSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]


class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.select_related(
        "rack",
        "rack__floor",
        "rack__floor__branch",
    )

    serializer_class = ShelfSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]
