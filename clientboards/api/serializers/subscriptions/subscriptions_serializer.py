from rest_framework import serializers

from clientboards.api.models.subscriptions.models import Subscriptions


class SubscriptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['id', 'account_id', 'subscription_plan', 'start_date', 'end_date',
                  'status', 'billing_cycle', 'billing_amount', 'payment_method', 'trial_period']
        read_only_fields = ['subscription_plan', 'start_date', 'status',
                            'billing_cycle', 'billing_amount', 'payment_method', 'trial_period']
