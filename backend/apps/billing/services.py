from datetime import date

from .models import BillingCycle


class BillingService:
    @staticmethod
    def generate_bill(subscription):

        month_start = date.today().replace(day=1)

        exists = BillingCycle.objects.filter(
            subscription=subscription, billing_month=month_start
        ).exists()

        if exists:
            return

        BillingCycle.objects.create(
            subscription=subscription,
            billing_month=month_start,
            amount=subscription.plan.monthly_fee,
        )
