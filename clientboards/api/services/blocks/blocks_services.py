import json
from urllib.parse import unquote

# models
from clientboards.api.models.blocks.models import Blocks

# serializers
from clientboards.api.serializers.blocks.blocks_serializer import BlocksSerializer


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

        blocksQuerySet = Blocks.objects.filter(user_id=userId, **filters)
        blocksSerializer = BlocksSerializer(blocksQuerySet, many=True)
        return blocksSerializer.data
