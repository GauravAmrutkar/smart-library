from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BookListView,
    InventoryCreateView,
    InventoryListView,
    InventoryUpdateView,
    PublisherViewSet,
)

router = DefaultRouter()

router.register(
    "publishers",
    PublisherViewSet,
    basename="publisher",
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path(
        "inventory/",
        InventoryListView.as_view(),
        name="inventory-list",
    ),
    path(
        "inventory/create/",
        InventoryCreateView.as_view(),
        name="inventory-create",
    ),
    path(
        "inventory/<int:pk>/",
        InventoryUpdateView.as_view(),
        name="inventory-update",
    ),
    path("", include(router.urls)),
]
