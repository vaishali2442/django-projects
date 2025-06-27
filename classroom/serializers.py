from rest_framework import serializers
from .models import grade , section , studentdetails,teacherdetails,attendance

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = grade
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentdetails
        fields = '__all__'

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacherdetails
        fields = '__all__'

class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = attendance