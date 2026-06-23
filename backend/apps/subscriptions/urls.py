from django.urls import path

from .views import SubscriptionPlanListView, UserSubscriptionListView

urlpatterns = [
    path("plans/", SubscriptionPlanListView.as_view()),
    path("user-subscriptions/", UserSubscriptionListView.as_view()),
]
