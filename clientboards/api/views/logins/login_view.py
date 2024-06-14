from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.logins.login_services import LoginServices


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        return ResponseGenerator(lambda: LoginServices.login(request=request, email=request.data.get('email'), password=request.data.get('password')))
