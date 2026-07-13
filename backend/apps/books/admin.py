from django.contrib import admin

from .models import (
    Author,
    Book,
    BookImage,
    Category,
    Inventory,
    Language,
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


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "code",
    )

    search_fields = (
        "name",
        "code",
    )


class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "edition",
        "author",
        "publisher",
        "language",
        "status",
        "price",
    )

    search_fields = (
        "title",
        "isbn_13",
    )

    list_filter = (
        "status",
        "cover_type",
        "category",
        "publisher",
        "language",
    )

    inlines = [
        BookImageInline,
    ]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "library_stock",
        "available_library_stock",
        "store_stock",
        "available_store_stock",
    )
