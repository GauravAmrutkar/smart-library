from rest_framework import serializers

from .models import Author, Book, Category, Inventory


def validate(self, attrs):

    if attrs["available_library_stock"] > attrs["library_stock"]:
        raise serializers.ValidationError(
            "Available library stock cannot exceed total stock"
        )

    if attrs["available_store_stock"] > attrs["store_stock"]:
        raise serializers.ValidationError(
            "Available store stock cannot exceed total stock"
        )

    return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class InventoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            "library_stock",
            "available_library_stock",
            "store_stock",
            "available_store_stock",
        )


class BookSerializer(serializers.ModelSerializer):
    inventry = InventoryNestedSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
