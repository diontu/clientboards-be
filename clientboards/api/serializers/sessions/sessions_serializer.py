from rest_framework import serializers

from clientboards.api.models import Sessions


class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = '__all__'
