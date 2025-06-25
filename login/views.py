from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import users
# Create your views here.
@api_view(['POST'])
def login(request):
    try:
        bodyData = request.data
        if not bodyData.user_email:
            return Response({
                'message':'Please Provide User Name',
                'status':400,
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not bodyData.user_password:
            return Response({
                'message':'Please Provide Password',
                'status':400,
            }, status=status.HTTP_400_BAD_REQUEST)
        userAuth = users.objects.filter(user_email = bodyData.user_email,password =bodyData.user_password ).first()
        if userAuth:
            return Response({
                'message':'Login Successfull',
                'status':400,
            }, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({
                'message':f'{str(error)}',
                'status':500,
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
