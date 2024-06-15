from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

# response structure
from clientboards.api.response.response import ResponseStructure

defaultMessage = "An error occurred"
defaultStatus = status.HTTP_500_INTERNAL_SERVER_ERROR


class AuthenticationError(AuthenticationFailed):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Invalid authentication credentials provided.'
    default_code = 'authentication_failed'

    def __init__(self, detail=None):
        if detail is None:
            detail = self.default_detail

        self.detail = ResponseStructure(detail, self.status_code)
