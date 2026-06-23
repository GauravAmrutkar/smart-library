from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import BorrowService


class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        book_id = request.data.get("book_id")

        transaction = BorrowService.borrow_book(request.user, book_id)

        return Response(
            {"message": "Book borrowed successfully", "transaction_id": transaction.id}
        )
