from rest_framework import serializers

from clientboards.api.models.block_permissions.models import BlockPermissions


class BlockPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockPermissions
        fields = '__all__'
