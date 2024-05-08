import json

from rest_framework import status

# models
from clientboards.api.models.accounts.models import Accounts

# serializers
from clientboards.api.serializers.accounts.accounts_serializer import AccountsSerializer

# errors
from clientboards.api.services.ServicesError import ServicesError

# services
from clientboards.api.services.users.users_services import UsersServices


class AccountsServices():
    # TODO: find out what the type for this could be.
    @staticmethod
    def getAccounts():
        accountQuerySet = Accounts.objects.all()
        accountSerializer = AccountsSerializer(accountQuerySet, many=True)
        return accountSerializer.data

    @staticmethod
    def createAccount(email: str, password: str, country: str) -> Accounts:
        print('logger: attempting to create an account')
        # create the user
        savedUser = UsersServices.createUser(email, password, country)

        # then create the account
        accountData = {
            "user_id": savedUser.id,
            "attributes": json.dumps({})
        }
        accountSerializer = AccountsSerializer(data=accountData)
        if not accountSerializer.is_valid():
            print('logger: account is not valid')
            raise ServicesError(message="account is not valid",
                                details=accountSerializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

        savedAccount = accountSerializer.save()

        if not isinstance(savedAccount, Accounts):
            raise ServicesError(message="Not an account",
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return savedAccount
