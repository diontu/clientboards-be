import bcrypt
from rest_framework import status

# models
from clientboards.api.models.users.models import Users

# serializers
from clientboards.api.serializers.users.users_serializer import UsersSerializer

# errors
from clientboards.api.services.ServicesError import ServicesError


class UsersServices():
    @staticmethod
    def getUsers():
        usersQuerySet = Users.objects.all()
        userSerializer = UsersSerializer(usersQuerySet, many=True)
        return userSerializer.data

    @staticmethod
    def createUser(email: str, password: str, country: str) -> Users:
        print('logger: attempting to create an user')
        # create the user
        userQuerySet = Users.objects.filter(
            email__exact=email)
        if userQuerySet.count() > 0:
            print('logger: user already exists')
            raise ServicesError(
                message='User already exists', status_code=status.HTTP_400_BAD_REQUEST)

        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        userData = {
            "email": email,
            "password": hashed_password,
            "country": country
        }
        userSerializer = UsersSerializer(data=userData)
        if not userSerializer.is_valid():
            print('logger: user is not valid')
            raise ServicesError(details=userSerializer.errors,
                                status_code=status.HTTP_400_BAD_REQUEST)

        print('logger: user is valid')
        savedUser = userSerializer.save()

        if not isinstance(savedUser, Users):
            raise ServicesError(
                message="Not a user", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return savedUser
