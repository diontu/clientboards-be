from rest_framework import status
from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# errors
from clientboards.api.services.ServicesError import ServicesError


class LoginAPIView(APIView):
    def postResponseData(self, request):
        if request.user is not None:
            return 'Login successful'
        else:
            raise ServicesError(message='Login failed',
                                status_code=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        return ResponseGenerator(lambda: self.postResponseData(request))
