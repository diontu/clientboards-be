from rest_framework import serializers

# security
from clientboards.api.security.security import verifyPasswordHash


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    # TODO: add validation to the email field and the password field (too short)

    def validate_password(self, password):
        if len(password) < 4:
            raise serializers.ValidationError(
                'Password must be at least 4 characters long')

        return password

    def validate_email(self, email):
        if len(email) < 4:
            raise serializers.ValidationError(
                'Email must be at least 4 characters long')

        return email

    def create(self, validated_data):
        """
        Create a login serializer. Returns True if the login is valid. False otherwise.
        """
        email = validated_data.get('email')
        password = validated_data.get('password')

        if verifyPasswordHash(password, email):
            return True
        else:
            return False
