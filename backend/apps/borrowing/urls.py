from django.urls import path

from .views import BorrowBookView

urlpatterns = [
    path("borrow/", BorrowBookView.as_view()),
]
