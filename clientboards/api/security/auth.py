import base64

from rest_framework import status
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from clientboards.api.security.auth_error import AuthenticationError

# services
from clientboards.api.services.logins.login_services import LoginServices

# errors
from clientboards.api.services.ServicesError import ServicesError


class Auth(BaseAuthentication):

    def authenticate(self, request):
        authHeader = get_authorization_header(request).decode('utf-8')
        if authHeader and authHeader.startswith('Basic '):
            return self._authenticateBasic(authHeader)
        else:
            return self._authenticateEmailPassword(request)

    def _authenticateBasic(self, authHeader):
        try:
            auth = authHeader.split(' ')[1]
            email, password = base64.b64decode(auth).decode('utf-8').split(':')

            if not email or not password:
                raise AuthenticationError('Invalid credentials')

            user, *rest = LoginServices.login(email, password)
        except ServicesError as se:
            raise AuthenticationError(se.details)
        except Exception:
            raise AuthenticationError('Invalid credentials')

        return (user, None)

    def _authenticateEmailPassword(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            if not email or not password:
                raise AuthenticationError('Invalid credentials')

            user, *rest = LoginServices.login(email, password)
        except ServicesError as se:
            raise AuthenticationError(se.details)
        except Exception:
            raise AuthenticationError('Invalid credentials')

        return (user, None)
