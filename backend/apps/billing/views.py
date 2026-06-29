from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import BillingCycle
from .serializers import BillingCycleSerializer


class MyBillsView(generics.ListAPIView):
    serializer_class = BillingCycleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BillingCycle.objects.filter(subscription__user=self.request.user)
