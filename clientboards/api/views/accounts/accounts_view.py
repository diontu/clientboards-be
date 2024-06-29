# type: ignore

from django.forms.models import model_to_dict
from django.http import HttpRequest

# rest
from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.accounts.accounts_services import AccountsServices


class AccountsAPIView(APIView):
    def get(self, request: HttpRequest):
        if request.user is not None:
            return ResponseGenerator(lambda: model_to_dict(AccountsServices.getAccountByUserId(userId=request.user.id)))
