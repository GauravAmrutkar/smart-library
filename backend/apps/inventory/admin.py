from django.contrib import admin

from .models import LibraryBranch


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

    ordering = (
        "name",
    )