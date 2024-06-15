from django.forms.models import model_to_dict
from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# auth
from clientboards.api.security.auth import Auth

# services
from clientboards.api.services.accounts.accounts_services import AccountsServices


class AccountsAPIView(APIView):
    authentication_classes = [Auth]

    def get(self, request):
        return ResponseGenerator(lambda: AccountsServices.getAccounts())

    def postResponseData(self, request):
        createdAccountModel = AccountsServices.createAccount(
            email=request.data.get('email'),
            password=request.data.get('password'),
            country=request.data.get('country')
        )
        return model_to_dict(createdAccountModel)

    def post(self, request, *args, **kwargs):
        return ResponseGenerator(lambda: self.postResponseData(request))
