from rest_framework import serializers

from .models import BorrowTransaction


class BorrowTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowTransaction
        fields = "__all__"
        read_only_fields = (
            "user",
            "status",
            "borrow_date",
        )
