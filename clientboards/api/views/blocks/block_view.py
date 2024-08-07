# type: ignore

from django.http import HttpRequest

# rest
from rest_framework.views import APIView

# repsonse
from clientboards.api.response.response import ResponseGenerator

# services
from clientboards.api.services.blocks.blocks_services import BlockServices


class BlocksAPIView(APIView):
    def get(self, request: HttpRequest):
        # get the blocks filter from the URL query params
        blocks_filter = request.GET.get('blocks_filter')
        return ResponseGenerator(lambda: BlockServices.getBlocksByUserId(userId=request.user.id, blocksFilter=blocks_filter))

    def post(self, request: HttpRequest):
        filter = {
            'block_id': request.data.get('block_id'),
            'owner_id': request.data.get('owner_id'),
            'type': request.data.get('type'),
            'properties': request.data.get('properties'),
            'content': request.data.get('content'),
            'parent_block_id': request.data.get('parent_block_id')
        }
        return ResponseGenerator(lambda: BlockServices.saveBlock(user_id=request.user.id, **filter))
