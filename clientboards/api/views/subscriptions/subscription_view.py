from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.subscriptions.subscription_services import (
    SubscriptionsServices,
)


class SubscriptionsAPIView(APIView):
    def get(self, request):
        return ResponseGenerator(lambda: SubscriptionsServices.getSubscriptions())

    def post(self, request):
        return ResponseGenerator(lambda: SubscriptionsServices.createSubscription())
