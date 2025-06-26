from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import grade,section,studentdetails,teacherdetails
from django.utils import timezone
from .serializers import GradeSerializer, SectionSerializer,StudentDetailSerializer,TeacherDetailSerializer

class GradeView(APIView):

    def create(self,request):
        try:
            serializer = GradeSerializer(data = request.data)
            if serializer.is_valid(): 
                serializer.save()           
                return Response({
                    'message':"Grade create successfully",
                    'status':200
                },status = status.HTTP_200_CREATED)
            else:
                return Response({
                    'message':"Error while creating grade",
                    'status':500
                },status = status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response({
                'message':f'{str(error)}',
                'status':500
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self,request):
        try:
            gradeData = grade.objects.all()
            if gradeData:
                serializer = GradeSerializer(data = gradeData,many=True)
                if serializer.is_valid(): 
                    serializer.save()           
                    return Response({
                        'message':"Grade data retrieved successfully",
                        'status':200,
                        'result':serializer.data
                    },status = status.HTTP_201_OK)
                else:
                    return Response({
                        'message':"Error while getting grade",
                        'status':400
                    },status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'message':"No data found",
                    'status':200
                },status = status.HTTP_200_OK)

        except Exception as error:
            return Response({
                'message':f'{str(error)}',
                'status':500
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def update(self,request):
        try:
            grade_id = request.query_params.get('grade_id')
            gradeData = grade.objects.filter(grade_id = grade_id)
            if gradeData:
                serializer = GradeSerializer(gradeData,data = request.data)
                if serializer.is_valid(): 
                    serializer.save()           
                    return Response({
                        'message':"Grade data retrieved successfully",
                        'status':200
                    },status = status.HTTP_201_OK)
                else:
                    return Response({
                        'message':"Error while getting grade",
                        'status':400
                    },status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'message':"No grade found to update",
                    'status':200
                },status = status.HTTP_200_OK)

        except Exception as error:
            return Response({
                'message':f'{str(error)}',
                'status':500
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request):
        try:
            grade_id = request.query_params.get('grade_id')
            gradeData = grade.objects.filter(grade_id = grade_id)
            if gradeData:
                gradeData.delete()
                return Response({
                    'message':"Grade deleted successfully",
                    'status':200
                },status = status.HTTP_201_OK)
            else:
                return Response({
                    'message':"No grade found to delete",
                    'status':200
                },status = status.HTTP_200_OK)

        except Exception as error:
            return Response({
                'message':f'{str(error)}',
                'status':500
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    

        
    
