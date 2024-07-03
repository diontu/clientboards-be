import json
from urllib.parse import unquote

from rest_framework import status

# models and services
from clientboards.api.models.blocks.models import Blocks, BlockType

# serializers
from clientboards.api.serializers.blocks.blocks_serializer import BlocksSerializer
from clientboards.api.services.block_permissions.block_permissions_services import (
    BlockPermissionsServices,
)

# errors
from clientboards.api.services.ServicesError import ServicesError

# tasks
from clientboards.api.tasks.tasks import saveBlock as saveBlockTask


class BlockServices:
    @staticmethod
    def getBlocksByUserId(userId: int, blocksFilter: str | None = None):
        # return all blocks based on the filters
        blocksFilterDict: dict = {}
        if blocksFilter is not None:
            blocksFilterDict = json.loads(unquote(blocksFilter))

        filters = {}
        if 'id' in blocksFilterDict and blocksFilterDict['id'] is not None:
            filters['id'] = int(blocksFilterDict['id'])
        if 'type' in blocksFilterDict and blocksFilterDict['type'] is not None:
            filters['type'] = blocksFilterDict['type']

        if not BlockPermissionsServices.canUserRead(user_id=userId, block_id=filters['id']):
            raise ServicesError(message='You do not have permission to read this block',
                                status_code=status.HTTP_403_FORBIDDEN)

        blocksQuerySet = Blocks.objects.filter(user_id=userId, **filters)
        blocksSerializer = BlocksSerializer(blocksQuerySet, many=True)
        return blocksSerializer.data

    @staticmethod
    def saveBlock(user_id: int, owner_id: int, type: str, block_id: int, properties: dict | None = None, content: str | None = None, parent_block_id: int | None = None):
        if not BlockServices.validateBlockType(type=type):
            raise ServicesError(message='Invalid block type',
                                status_code=status.HTTP_400_BAD_REQUEST)

        if not BlockPermissionsServices.canUserWrite(
                user_id=user_id, block_id=block_id):
            raise ServicesError(message='You do not have permission to write to this block',
                                status_code=status.HTTP_403_FORBIDDEN)

        saveBlockTask.delay(user_id=user_id, type=type, owner_id=owner_id, block_id=block_id, properties=properties,
                            content=content, parent_block_id=parent_block_id)
        return 'Block successfully queued for saving'

    @staticmethod
    def validateBlockType(type: str) -> bool:
        if type in [block.value for block in BlockType]:
            return True
        return False
