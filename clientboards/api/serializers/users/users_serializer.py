from rest_framework import serializers

from clientboards.api.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['last_login', 'date_created']
