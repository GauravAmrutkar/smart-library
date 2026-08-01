from django.contrib import admin

from .models import BookCopy, Floor, LibraryBranch, Rack, Shelf


@admin.register(LibraryBranch)
class LibraryBranchAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "city",
        "state",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "city",
    )

    list_filter = (
        "state",
        "is_active",
    )

    ordering = ("name",)


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "branch",
        "code",
    )

    list_filter = ("branch",)

    search_fields = (
        "name",
        "code",
    )


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    list_display = (
        "branch",
        "name",
        "code",
        "is_active",
    )

    list_filter = (
        "branch",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = (
        "rack",
        "name",
        "code",
        "capacity",
        "is_active",
    )

    list_filter = (
        "rack",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    ordering = (
        "rack",
        "name",
    )


@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = (
        "accession_number",
        "book",
        "status",
        "condition",
        "shelf",
    )

    readonly_fields = (
        "accession_number",
        "barcode",
    )

    list_filter = (
        "status",
        "condition",
        "shelf",
    )

    search_fields = (
        "accession_number",
        "barcode",
        "book__title",
    )
