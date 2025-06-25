from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import users , roles
from django.utils import timezone
from serializers import UserSerializer,RoleSerializer


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


@api_view(['POST'])
def createRole(request):
    try:
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide role name'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = RoleSerializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
            'status': 201,
            'message': 'Role created successfully',
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
            'status': 400,
            'message': 'Facing Issue While Creating Role..',
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updateRole(request):
    try:
        role_id = request.query_param.get('role_id')
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide role name'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        roleInstance = roles.objects.filter(role_id = role_id).first()
        if not roleInstance:
            return Response({
            'status': 400,
            'message': f'Cannot find data with this role id {role_id}..',
        }, status=status.HTTP_400_BAD_REQUEST)

        serializer = RoleSerializer(roleInstance, data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
            'status': 201,
            'message': 'Role updating successfully',
            }, status=status.HTTP_200_OK)
        else:
            return Response({
            'status': 400,
            'message': 'Facing Issue While Creating Role..',
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getRole(request):
    try:
        role_id = request.query_param.get('role_id')
        if role_id:
            roleInstance = roles.objects.filter(role_id=role_id).first()
            serializer = RoleSerializer(roleInstance)
            return Response({
                'status': 200,
                'message': 'Role data found successfully',
                'result' : serializer.data
                }, status=status.HTTP_201_OK)
        else:
            roleInstance = roles.objects.all()
            if not roleInstance.exists():
                return Response({
                    'status': 400,
                    'message': f'Cannot find data',
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = RoleSerializer(roleInstance,many=True)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'Role data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_201_OK)
    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
def deleteRole(request):
    try:
        role_id = request.query_param.get('role_id')
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide role id'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        roleInstance = roles.objects.filter(role_id = role_id).first()
        if not roleInstance:
            return Response({
            'status': 400,
            'message': f'Cannot find data with this role id {role_id}..',
        }, status=status.HTTP_400_BAD_REQUEST)

        roleInstance.delete()
        return Response({
        'status': 201,
        'message': 'Role deleted successfully',
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['POST'])
def createUser(request):
    try:
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide user data'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
            'status': 201,
            'message': 'User created successfully',
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
            'status': 400,
            'message': 'Facing Issue While Creating User..',
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updateUsers(request):
    try:
        user_id = request.query_param.get('user_id')
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide user id'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        userInstance = users.objects.filter(user_id = user_id).first()
        if not userInstance:
            return Response({
            'status': 400,
            'message': f'Cannot find data with this user id {user_id}..',
        }, status=status.HTTP_400_BAD_REQUEST)

        serializer = RoleSerializer(userInstance, data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
            'status': 201,
            'message': 'User updating successfully',
            }, status=status.HTTP_200_OK)
        else:
            return Response({
            'status': 400,
            'message': 'Facing Issue While Creating Role..',
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getUsers(request):
    try:
        user_id = request.query_params.get('user_id')
        if user_id:
            userInstance = users.objects.filter(user_id=user_id).first()
            serializer = RoleSerializer(userInstance)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'user data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_201_OK)
        else:
            userInstance = users.objects.all()
            if not userInstance.exists():
                return Response({
                    'status': 400,
                    'message': f'Cannot find data',
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = RoleSerializer(userInstance,many=True)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'user data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_201_OK)
    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
def deleteUser(request):
    try:
        user_id = request.query_param.get('user_id')
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide user id'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        userInstance = users.objects.filter(user_id = user_id).first()
        if not userInstance:
            return Response({
            'status': 400,
            'message': f'Cannot find data with this user id {user_id}..',
        }, status=status.HTTP_400_BAD_REQUEST)

        userInstance.delete()
        return Response({
        'status': 201,
        'message': 'user deleted successfully',
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




