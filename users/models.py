from django.db import models
from django.utils import timezone

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    user_id =  models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=200,null=True,blank=True)
    role_id = models.ForeignKey(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name or f"User {self.user_id}"


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name or f"Role {self.role_id}"
