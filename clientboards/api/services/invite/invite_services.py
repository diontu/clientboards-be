# models
from clientboards.api.models import Users

# services and errors
from clientboards.api.services.block_permissions.block_permissions_services import (
    BlockPermissionsServices,
)
from clientboards.api.services.ServicesError import ServicesError


class InviteServices:
    @staticmethod
    def inviteUser(user_id: int, email: str, block_id: int, permission_type: str, additional_conditions: dict):
        user = Users.objects.filter(email=email)
        if user.count() == 0:
            raise ServicesError(message='User does not exist')

        user = user.first()

        if user is None:
            raise ServicesError(message='User does not exist')

        BlockPermissionsServices.setPermissions(
            block_id=block_id, user_id=user.id, owner_id=user_id, permission_type=permission_type, additional_conditions=additional_conditions)

        return 'successfully invited user'
