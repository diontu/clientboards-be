from typing import Optional

from celery import shared_task
from rest_framework import status

# models
from clientboards.api.models import Blocks

# serializers
from clientboards.api.serializers.blocks.blocks_serializer import BlocksSerializer
from clientboards.api.services.block_permissions.block_permissions_services import (
    BlockPermissionsServices,
)

# services
from clientboards.api.services.ServicesError import ServicesError


@shared_task
def log(message):
    print(message)


@shared_task
def add(one, two):
    return one + two


@shared_task
def saveBlock(user_id: int, owner_id: int, type: str, block_id: str, properties: Optional[dict] = None, content: Optional[str] = None, parent_block_id: Optional[Blocks] = None):
    # check if the block exists, if not create it
    blockQuerySet = Blocks.objects.filter(
        id__exact=block_id)

    fieldsToSave = {
        'type': type,
        'properties': properties if properties is not None else {},
        'content': content if content is not None else '',
        'parent_id': parent_block_id
    }
    if blockQuerySet.count() > 0:
        block = blockQuerySet.first()
        if block is None:
            raise ServicesError(message='Block does not exist')

        print('logger: block already exists')
        # make sure the block belongs to the user
        if block.owner_id != user_id:
            raise ServicesError(
                message='Block does not belong to the user',
            )

        block.type = fieldsToSave['type']
        block.properties = fieldsToSave['properties']
        block.content = fieldsToSave['content']
        block.parent_block_id = fieldsToSave['parent_block_id']  # type: ignore

        savedBlock = block.save()

        BlockPermissionsServices.setDefaultPermissions(
            block_id=block_id, user_id=user_id, owner_id=owner_id)
    else:
        # create the block
        block = {
            'owner_id': user_id,
            'id': block_id,
            **fieldsToSave,
        }
        blockSerializer = BlocksSerializer(data=block, many=False)
        if not blockSerializer.is_valid():
            raise ServicesError(details=blockSerializer.errors,
                                status_code=status.HTTP_400_BAD_REQUEST)

        savedBlock = blockSerializer.save()

        if not isinstance(savedBlock, Blocks):
            raise ServicesError(
                message='Not a block', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        BlockPermissionsServices.setDefaultPermissions(
            block_id=block_id, user_id=user_id, owner_id=owner_id)

    print('logger: block saved successfully')
