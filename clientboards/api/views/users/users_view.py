from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.users.users_services import UsersServices


class UsersAPIView(APIView):
    def get(self, request):
        return ResponseGenerator(lambda: UsersServices.getUsers())
