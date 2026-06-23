from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import AdminDashboardView, ProfileView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("admin-dashboard/", AdminDashboardView.as_view()),
]
