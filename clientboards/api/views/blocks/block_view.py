from rest_framework import generics

from clientboards.api.models.blocks.models import Blocks
from clientboards.api.serializers.blocks.blocks_serializer import BlocksSerializer


class BlocksAPIView(generics.ListAPIView):
    queryset = Blocks.objects.all()
    serializer_class = BlocksSerializer
