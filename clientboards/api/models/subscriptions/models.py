from django.db import models

from clientboards.api.models.users.models import Users


class SubscriptionStatus(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

# Create your models here.


class Subscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='subscriptions')
    subscription_plan = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(
        max_length=10, choices=SubscriptionStatus.choices)
    # monthly, yearly
    billing_cycle = models.CharField(max_length=20)
    billing_amount = models.DecimalField(decimal_places=2, max_digits=10)
    payment_method = models.CharField(max_length=30)
    # trial period is days
    trial_period = models.IntegerField(default=14)
