# myapp/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from users.models import users 
from rest_framework import serializers 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'user_email'

    def validate(self, attrs):
        email = attrs.get('user_email')
        password = attrs.get('password')

        user = users.objects.filter(user_email=email, password=password).first()
        if user is None:
            raise serializers.ValidationError('Invalid credentials')

        refresh = self.get_token(user)
        refresh['user_id'] = user.user_id
        refresh['user_email'] = user.user_email
        refresh['role'] = user.role.role_name if user.role else None

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.user_id,
            'user_email': user.user_email,
            'role': user.role.role_name if user.role else None
        }

        return data

