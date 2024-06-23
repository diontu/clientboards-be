from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.users.users_services import UsersServices

# tasks
from clientboards.api.tasks.tasks import log, add


class UsersAPIView(APIView):
    def get(self, request):
        # TODO: remove below code. it is just for testing tasks
        result = add.delay(1, 2)
        log.delay('logger: nice')
        print('task nice:', result.id)
        return ResponseGenerator(lambda: UsersServices.getUsers())
