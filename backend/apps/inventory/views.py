from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.permissions import IsAdminUserRole

from .models import LibraryBranch
from .serializers import LibraryBranchSerializer


class LibraryBranchViewSet(viewsets.ModelViewSet):
    queryset = LibraryBranch.objects.all()

    serializer_class = LibraryBranchSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]