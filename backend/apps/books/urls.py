from django.urls import path

from .views import (
    BookListView,
    InventoryCreateView,
    InventoryListView,
    InventoryUpdateView,
)

urlpatterns = [
    path("", BookListView.as_view()),
    path("inventory/", InventoryListView.as_view()),
    path("inventory/create/", InventoryCreateView.as_view()),
    path("inventory/<int:pk>/", InventoryUpdateView.as_view()),
]
