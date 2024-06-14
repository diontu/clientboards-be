from datetime import datetime, timedelta

from rest_framework import status

from clientboards.api.models.sessions.models import Sessions

# models
from clientboards.api.models.users.models import Users

# serializers
from clientboards.api.serializers.accounts.login_serializer import LoginSerializer
from clientboards.api.serializers.sessions.sessions_serializer import SessionsSerializer

# errors
from clientboards.api.services.ServicesError import ServicesError


class LoginServices():
    @staticmethod
    def login(request, email: str, password: str):
        """
        Creates a session model and return it.
        """
        loginSerializer = LoginSerializer(
            data={'email': email, 'password': password})

        if not loginSerializer.is_valid() and not loginSerializer.save():
            print('logger: login is not valid')
            raise ServicesError(
                message=f'Login is not valid. errors: {loginSerializer.errors}', status_code=status.HTTP_400_BAD_REQUEST)

        # create the session
        try:
            user = Users.objects.get(email=email)
        except Exception:
            print('logger: user does not exist')
            raise ServicesError(
                message="User does not exist", status_code=status.HTTP_400_BAD_REQUEST)

        # check if the user has a session or not, given their email. If so, then return that session.
        sessionsQuerySet = Sessions.objects.filter(
            user_id__exact=user.id)

        hasExistingSession = sessionsQuerySet.first()

        if hasExistingSession:
            print('logger: user already has a session')
            return hasExistingSession

        # TODO: differentiate it by ip address in the future.

        currentTime = datetime.now()
        sessionExpiry = currentTime + timedelta(days=60)
        sessionData = {'user_id': user.id,
                       'start_date': currentTime, 'end_date': sessionExpiry}
        sessionSerializer = SessionsSerializer(data=sessionData)

        if not sessionSerializer.is_valid():
            print('logger: session is not valid')
            raise ServicesError(
                message="Session is not valid", details=sessionSerializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

        savedSession = sessionSerializer.save()

        if not isinstance(savedSession, Sessions):
            raise ServicesError(
                message="Not a Session", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return savedSession

    @staticmethod
    def logout():
        pass
