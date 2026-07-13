from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LibraryBranchViewSet

router = DefaultRouter()

router.register(
    "branches",
    LibraryBranchViewSet,
    basename="branch",
)

urlpatterns = [
    path("", include(router.urls)),
]