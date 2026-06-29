from django.db import models

from apps.subscriptions.models import UserSubscription


class BillingCycle(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PAID = "PAID", "Paid"
        CANCELLED = "CANCELLED", "Cancelled"

    subscription = models.ForeignKey(
        UserSubscription, on_delete=models.CASCADE, related_name="billing_cycles"
    )

    billing_month = models.DateField()

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    generated_on = models.DateTimeField(auto_now_add=True)

    paid_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-billing_month"]
        constraints = [
            models.UniqueConstraint(
                fields=["subscription", "billing_month"],
                name="unique_subscription_month",
            )
        ]

    def __str__(self):
        return f"{self.subscription.user.username} - {self.billing_month}"
