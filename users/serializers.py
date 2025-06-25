from rest_framework import serializers
from models import roles ,users

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = 'roles'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = 'users'