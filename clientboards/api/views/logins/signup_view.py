from django.forms.models import model_to_dict

# rest
from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.accounts.accounts_services import AccountsServices


class SignupAPIView(APIView):
    authentication_classes = []

    def postResponseData(self, request):
        createdAccountModel = AccountsServices.createAccount(
            email=request.data.get('email'),
            password=request.data.get('password'),
            country=request.data.get('country')
        )
        return model_to_dict(createdAccountModel)

    def post(self, request, *args, **kwargs):
        return ResponseGenerator(lambda: self.postResponseData(request))
