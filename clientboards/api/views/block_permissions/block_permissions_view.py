from rest_framework import generics

from clientboards.api.models.block_permissions.models import BlockPermissions
from clientboards.api.serializers.block_permissions.block_permissions_serializer import (
    BlockPermissionsSerializer,
)


class BlockPermissionsAPIView(generics.ListAPIView):
    queryset = BlockPermissions.objects.all()
    serializer_class = BlockPermissionsSerializer
