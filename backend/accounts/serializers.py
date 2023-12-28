from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ["id", "user_id", "phone", "birth_date"]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]
