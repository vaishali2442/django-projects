from rest_framework import serializers
from .models import roles ,users ,permissions

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = 'roles'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = 'users'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = 'permissions'