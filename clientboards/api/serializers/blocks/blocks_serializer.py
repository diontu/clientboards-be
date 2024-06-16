from rest_framework import serializers

from clientboards.api.models import Blocks


class BlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocks
        fields = '__all__'
