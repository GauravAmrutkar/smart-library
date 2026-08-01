from rest_framework import serializers

from .models import BorrowTransaction


class BorrowTransactionSerializer(serializers.ModelSerializer):

    book_title = serializers.CharField(
        source="book.title",
        read_only=True,
    )

    accession_number = serializers.CharField(
        source="book_copy.accession_number",
        read_only=True,
    )

    barcode = serializers.CharField(
        source="book_copy.barcode",
        read_only=True,
    )

    class Meta:

        model = BorrowTransaction

        fields = (
            "id",
            "book",
            "book_title",
            "book_copy",
            "accession_number",
            "barcode",
            "borrow_date",
            "return_date",
            "status",
        )
