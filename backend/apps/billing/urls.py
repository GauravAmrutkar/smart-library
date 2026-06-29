from django.urls import path

from .views import MyBillsView

urlpatterns = [
    path("", MyBillsView.as_view(), name="my-bills"),
]
