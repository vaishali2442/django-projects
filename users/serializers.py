from rest_framework import serializers
from .models import roles ,users ,permissions

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = roles


class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()  

    class Meta:
        model = users
        fields = ['user_id', 'first_name', 'last_name', 'user_email', 'role', 'role_name', 'created_at', 'updated_at']

    def get_role_name(self, obj):
        return obj.role.role_name if obj.role else None


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = permissions