from rest_framework import serializers
from .models import grade , section , studentdetails,teacherdetails

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'grade'
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'section'
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'student_detail'
        fields = '__all__'

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'student_detail'
        fields = '__all__'