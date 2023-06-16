from rest_framework.serializers import ModelSerializer

from core.models import CustomUser, Order


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "first_name", "last_name", "is_active")


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "status",
            "body",
            "created",
            "updated",
            "deleted",
        )
