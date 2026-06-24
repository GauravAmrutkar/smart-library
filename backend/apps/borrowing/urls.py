from django.urls import path

from .views import BorrowBookView, BorrowHistoryView, ReturnBookView

urlpatterns = [
    path("borrow/", BorrowBookView.as_view()),
    path("return/", ReturnBookView.as_view()),
    path("history/", BorrowHistoryView.as_view()),
]
