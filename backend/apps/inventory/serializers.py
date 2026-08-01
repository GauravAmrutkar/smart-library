from rest_framework import serializers

from .models import BookCopy, Floor, LibraryBranch, Rack, Shelf


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


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor

        fields = (
            "id",
            "branch",
            "name",
            "code",
            "description",
        )


class RackSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(
        source="branch.name",
        read_only=True,
    )

    class Meta:
        model = Rack

        fields = (
            "id",
            "branch",
            "branch_name",
            "name",
            "code",
            "description",
            "is_active",
        )


class ShelfSerializer(serializers.ModelSerializer):
    rack_name = serializers.CharField(
        source="rack.name",
        read_only=True,
    )

    class Meta:
        model = Shelf

        fields = (
            "id",
            "rack",
            "rack_name",
            "name",
            "code",
            "description",
            "capacity",
            "is_active",
        )

class BookCopySerializer(serializers.ModelSerializer):

    book_title = serializers.CharField(
        source="book.title",
        read_only=True,
    )

    class Meta:

        model = BookCopy

        fields = (
            "id",
            "book",
            "book_title",
            "shelf",
            "accession_number",
            "barcode",
            "status",
            "condition",
            "purchase_date",
            "purchase_price",
            "supplier",
            "remarks",
        )

        read_only_fields = (
            "accession_number",
            "barcode",
        )