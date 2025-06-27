from django.db import models
from django.utils import timezone
# Create your models here.
class grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    grade_name = models.CharField(max_length=10,blank=True,null=True)
    created_at = models.DateField(default=timezone.now)
    updated_at =  models.DateField(default=timezone.now)

    class Meta:
        db_table = 'grade'

class section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10,blank=True,null=True)
    created_at = models.DateField(default=timezone.now)
    updated_at =  models.DateField(default=timezone.now)

    class Meta:
        db_table = 'section'


class studentdetails(models.Model):
    student_detail_id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=200,null=True,blank=True)
    grade_name = models.CharField(max_length=200,null=True,blank=True)
    section_name = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateField(default=timezone.now)
    updated_at =  models.DateField(default=timezone.now)

    class Meta:
        db_table = 'student_detail'


class teacherdetails(models.Model):
    teacher_detail_id = models.AutoField(primary_key=True)
    teacher_id = models.CharField(max_length=200,null=True,blank=True)
    grade_name = models.CharField(max_length=200,null=True,blank=True)
    section_name = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateField(default=timezone.now)
    updated_at =  models.DateField(default=timezone.now)

    class Meta:
        db_table = 'teacher_detail'


class attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    teacher_id = models.CharField(max_length=200,null=True,blank=True)
    student_name = models.CharField(max_length=200,null=True,blank=True)
    student_id = models.CharField(max_length=200,null=True,blank=True)
    grade_id = models.CharField(max_length=200,null=True,blank=True)
    grade_name = models.CharField(max_length=200,null=True,blank=True)
    section_id = models.CharField(max_length=200,null=True,blank=True)
    section_name = models.CharField(max_length=200,null=True,blank=True)
    attendance_status = models.CharField(max_length=200,null=True,blank=True)
    remark = models.TextField(null=True,blank=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'attendance'