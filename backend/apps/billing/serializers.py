from rest_framework import serializers

from .models import BillingCycle


class BillingCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingCycle
        fields = "__all__"
