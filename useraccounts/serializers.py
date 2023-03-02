from rest_framework import serializers

from useraccounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','confirm_password']
        extra_kwargs = {'password': {'write_only': True}}
        def create(self, validated_data):
            user=User.objects.create_user(**validated_data)
            return user