from django.contrib import admin

from .models import (
    Author,
    Book,
    Category,
    Inventory,
    Publisher,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )

    search_fields = ("name",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )

    search_fields = ("name",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
    )

    search_fields = (
        "name",
        "country",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "publisher",
        "category",
        "price",
    )

    search_fields = (
        "title",
        "isbn",
    )

    list_filter = (
        "category",
        "publisher",
    )


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "library_stock",
        "available_library_stock",
        "store_stock",
        "available_store_stock",
    )
