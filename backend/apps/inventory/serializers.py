from rest_framework import serializers

from .models import LibraryBranch


class LibraryBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBranch
        fields = (
            "id",
            "name",
            "code",
            "address",
            "city",
            "state",
            "postal_code",
            "phone",
            "email",
            "is_active",
        )