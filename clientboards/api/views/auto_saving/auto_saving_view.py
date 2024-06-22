from rest_framework import status
from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# errors
from clientboards.api.services.ServicesError import ServicesError


class AutoSaveAPIView(APIView):
    """
    Exceptions can be raised in the view, as long as the function that raises the error is being called inside a `ResponseGenerator`.
    """

    def postResponseData(self, request):
        # TODO: if it does not save to the task queue, then raise an error
        if True:
            pass
        else:
            raise ServicesError(message='Login failed',
                                status_code=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        return ResponseGenerator(lambda: self.postResponseData(request))
