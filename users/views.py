from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import users , roles
from django.utils import timezone


@api_view(['POST'])
def registerUser(request):
    try:
        data = request.data
        role_name = data.get('roleName')

        role = roles.objects.filter(role_name=role_name).first()
        if not role:
            return Response({
                'status': 400,
                'message': 'Invalid role name'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = users.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            role=role,  
            user_email=data.get('user_email'),
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

        return Response({
            'status': 201,
            'message': 'User created successfully',
            'user_id': user.id
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
