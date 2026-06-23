from rest_framework import generics

from .models import (
    SubscriptionPlan,
    UserSubscription,
)
from .serializers import SubscriptionPlanSerializer, UserSubscriptionSerializer


class SubscriptionPlanListView(generics.ListAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer


class UserSubscriptionListView(generics.ListAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
