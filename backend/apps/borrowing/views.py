from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BorrowTransaction
from .serializers import BorrowTransactionSerializer
from .services import BorrowService, ReturnService


class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        book_id = request.data.get("book_id")

        transaction = BorrowService.borrow_book(request.user, book_id)

        return Response(
            {"message": "Book borrowed successfully", "transaction_id": transaction.id}
        )


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        transaction_id = request.data.get("transaction_id")

        transaction_obj = ReturnService.return_book(
            request.user,
            transaction_id,
        )

        return Response(
            {
                "message": "Book returned successfully",
                "transaction_id": transaction_obj.id,
            }
        )


class BorrowHistoryView(generics.ListAPIView):
    serializer_class = BorrowTransactionSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BorrowTransaction.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )
