from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Added serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(  # Used get_user_model().objects.create_user
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Create auth token for user
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'date_joined']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)  # Added serializers.CharField()

