from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import users , roles,permissions
from classroom.models import teacherdetails,studentdetails,grade,section
from django.utils import timezone
from .serializers import UserSerializer,RoleSerializer,PermissionSerializer

# API FOR REGISTERING THE USERS
@api_view(['POST'])
def registerUser(request):
    try:
        data = request.data
        user = users.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            user_email=data.get('user_email'),
            phone_number = data.get('phone_number'),
            password = data.get('password'), 
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        return Response({
            'status': 201,
            'message': 'User created successfully',
            'user_id': user.user_id
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def mapUser(request):
    try:
        data = request.data
        roleName = data.get('role_name')
        user_id = data.get('user_id')
        grade_name = data.get('grade_name')
        section_name = data.get('section_name')
        if roleName == 'teacher':
            teacherData  = teacherdetails.objects.create(
                teacher_id=user_id,
                grade_name =grade_name,
                section_name=section_name,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

        if roleName == 'student':
            studentData  = studentdetails.objects.create(
                student_id=user_id,
                grade_name =grade_name,
                section_name=section_name,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
        role_instance = roles.objects.filter(role_name=roleName).first()
        if not role_instance:
            return Response({
                'status': 400,
                'message': f'Invalid role name: {roleName}'
            }, status=status.HTTP_400_BAD_REQUEST)
        user_instance = users.objects.filter(user_id=user_id).first()
        if not user_instance:
            return Response({
                'status': 400,
                'message': f'User with ID {user_id} not found'
            }, status=status.HTTP_400_BAD_REQUEST)

        user_instance.role = role_instance
        user_instance.updated_at = timezone.now()
        user_instance.save()
        return Response({
            'status': 201,
            'message': 'User created successfully',
            'user_id': user_id
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
        if serializer.is_valid():
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
        role_id = request.query_params.get('role_id')
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
        if serializer.is_valid():
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
        role_id = request.query_params.get('role_id')
        if role_id:
            roleInstance = roles.objects.filter(role_id=role_id).first()
            serializer = RoleSerializer(roleInstance)
            return Response({
                'status': 200,
                'message': 'Role data found successfully',
                'result' : serializer.data
                }, status=status.HTTP_200_OK)
        else:
            roleInstance = roles.objects.all()
            if not roleInstance.exists():
                return Response({
                    'status': 400,
                    'message': f'No data available',
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = RoleSerializer(roleInstance,many=True)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'Role data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
def deleteRole(request):
    try:
        role_id = request.query_params.get('role_id')
        if not role_id:
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
            serializer = UserSerializer(userInstance)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'user data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_200_OK)
        else:
            userInstance = users.objects.all()
            if not userInstance.exists():
                return Response({
                    'status': 400,
                    'message': f'Cannot find data',
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = UserSerializer(userInstance, many=True)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'user data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_200_OK)
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


# Permissions APIS
@api_view(['POST'])
def createPermissions(request):
    try:
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide user data'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = PermissionSerializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
            'status': 201,
            'message': 'permission created successfully',
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
            'status': 400,
            'message': 'Facing Issue While Creating Permission..',
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updatePermissions(request):
    try:
        permission_id = request.query_param.get('permission_id')
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide permission id'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        permissionInstance = users.objects.filter(permission_id = permission_id).first()
        if not permissionInstance:
            return Response({
            'status': 400,
            'message': f'Cannot find data with this permission id {permission_id}..',
        }, status=status.HTTP_400_BAD_REQUEST)

        serializer = PermissionSerializer(permissionInstance, data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
            'status': 201,
            'message': 'Permission updating successfully',
            }, status=status.HTTP_200_OK)
        else:
            return Response({
            'status': 400,
            'message': 'Facing Issue While Updating permission..',
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getPermissions(request):
    try:
        permission_id = request.query_params.get('permission_id')
        if permission_id:
            permissionInstance = users.objects.filter(permission_id=permission_id).first()
            serializer = PermissionSerializer(permissionInstance)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'permission data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_201_OK)
        else:
            permissionInstance = permissions.objects.all()
            if not permissionInstance.exists():
                return Response({
                    'status': 400,
                    'message': f'Cannot find data',
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = permissions(permissionInstance,many=True)
            if serializer.data:
                return Response({
                    'status': 200,
                    'message': 'permission data found successfully',
                    'result' : serializer.data
                    }, status=status.HTTP_201_OK)
    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
def deletePermissions(request):
    try:
        permission_id = request.query_param.get('permission_id')
        if not request.data:
            return Response({
                'status': 400,
                'message': 'Please Provide permission id'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        permissionInstance = users.objects.filter(permission_id = permission_id).first()
        if not permissionInstance:
            return Response({
            'status': 400,
            'message': f'Cannot find data with this permission id {permission_id}..',
        }, status=status.HTTP_400_BAD_REQUEST)

        permissionInstance.delete()
        return Response({
        'status': 201,
        'message': 'permission deleted successfully',
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            'status': 500,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




