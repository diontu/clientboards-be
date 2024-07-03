from rest_framework import status

from clientboards.api.models.block_permissions.models import (
    BlockPermissions,
    BlockPermissionsType,
)

# models
from clientboards.api.models.blocks.models import Blocks

# serializers
from clientboards.api.serializers.block_permissions.block_permissions_serializer import (
    BlockPermissionsSerializer,
)

# services
from clientboards.api.services.ServicesError import ServicesError


class BlockPermissionsServices:
    @staticmethod
    def setDefaultPermissions(block_id: int, user_id: int, owner_id: int):
        BlockPermissionsServices.setPermissions(
            block_id=block_id, user_id=user_id, owner_id=owner_id, permission_type=BlockPermissionsType.WRITE, additional_conditions={})

    @staticmethod
    def setPermissions(block_id: int, user_id: int, owner_id: int, permission_type: str, additional_conditions: dict):
        print('logger: attempting to save block permissions')
        # check if the block exists, if not raise a services error
        blocks = Blocks.objects.filter(id__exact=block_id)

        if blocks.count() == 0:
            print('logger: block does not exist')
            raise ServicesError(message='Block does not exist')

        # there should only be one permission for a block for each user
        permissions = BlockPermissions.objects.filter(
            block_id=block_id, user_id=user_id)

        if permissions.count() == 0:
            # set the default permissions as write
            permissionsToSave = {
                'block_id': block_id,
                'user_id': user_id,
                'owner_id': owner_id,
                'permission_type': permission_type,
                'additional_conditions': additional_conditions
            }
            serializer = BlockPermissionsSerializer(data=permissionsToSave)

            if not serializer.is_valid():
                print(serializer.errors)
                print('logger: block permission is not valid')
                raise ServicesError(message='Block permission is not valid', details=serializer.errors,
                                    status_code=status.HTTP_400_BAD_REQUEST)
            serializer.save()
        else:
            blockPermission = permissions.first()

            if blockPermission is None:
                print('logger: block permission does not exist')
                raise ServicesError(message='Block permission does not exist')

            permissionsToSave = {
                'permission_type': permission_type,
                'additional_conditions': additional_conditions
            }
            blockPermission.permission_type = permissionsToSave['permission_type']
            blockPermission.additional_conditions = permissionsToSave['additional_conditions']

            blockPermission.save()

        print('logger: block permissions saved successfully')

    @staticmethod
    def canUserRead(block_id: int, user_id: int):
        permissions = BlockPermissions.objects.filter(
            block_id=block_id, user_id=user_id, permission_type__in=[BlockPermissionsType.READ, BlockPermissionsType.WRITE])

        if permissions.count() == 0:
            return False
        else:
            return True

    @staticmethod
    def canUserWrite(block_id: int, user_id: int):
        permissions = BlockPermissions.objects.filter(
            block_id=block_id, user_id=user_id, permission_type=BlockPermissionsType.WRITE)

        if permissions.count() == 0:
            return False
        else:
            return True

    @staticmethod
    def isOwner(block_id: int, user_id: int):
        permissions = BlockPermissions.objects.filter(
            block_id=block_id, owner_id=user_id)

        if permissions.count() == 0:
            return False
        else:
            return True
