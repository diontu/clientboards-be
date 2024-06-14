from django.contrib.auth import authenticate, login, logout
from rest_framework import status

# serializers
from clientboards.api.serializers.accounts.login_serializer import LoginSerializer

# errors
from clientboards.api.services.ServicesError import ServicesError


class LoginServices():
    @staticmethod
    def login(request, email: str, password: str):
        loginSerializer = LoginSerializer(
            data={email: email, password: password})

        if not loginSerializer.is_valid():
            print('logger: login is not valid')
            raise ServicesError(
                message='Login is not valid', status_code=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user=user)
            return "Login successful"
        else:
            ServicesError(message="Invalid credentials",
                          status_code=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def logout():
        pass
