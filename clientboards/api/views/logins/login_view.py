from django.forms.models import model_to_dict
from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.logins.login_services import LoginServices


class LoginAPIView(APIView):
    def postResponseData(self, request):
        createdSessionModel = LoginServices.login(request=request, email=request.data.get(
            'email'), password=request.data.get('password'))

        # can't serialize a model so we convert it to a dict
        return model_to_dict(createdSessionModel)

    def post(self, request, *args, **kwargs):
        return ResponseGenerator(lambda: self.postResponseData(request))
