from django.conf import settings
from django.db import models


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50, unique=True)

    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)

    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)

    max_active_books = models.PositiveIntegerField()

    duration_days = models.PositiveIntegerField(default=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        EXPIRED = "EXPIRED", "Expired"
        CANCELLED = "CANCELLED", "Cancelled"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions"
    )

    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)

    start_date = models.DateField()

    end_date = models.DateField()

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ACTIVE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"
