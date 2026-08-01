from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LibraryBranchViewSet, RackViewSet, ShelfViewSet

router = DefaultRouter()

router.register(
    "branches",
    LibraryBranchViewSet,
    basename="branch",
)

router.register(
    "racks",
    RackViewSet,
    basename="rack",
)

router.register(
    "shelves",
    ShelfViewSet,
    basename="shelf",
)

urlpatterns = [
    path("", include(router.urls)),
]
