from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class users(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    user_id =  models.AutoField(primary_key=True)
    user_email = models.EmailField(unique=True, null=True, blank=True)
    role = models.ForeignKey("roles",on_delete=models.CASCADE,blank=True,null=True)
    password = models.CharField(max_length=200,null=True,blank=True)
    permission = models.ForeignKey('permissions',on_delete=models.CASCADE, default=1)
    phone_number = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name or f"User {self.user_id}"
    class Meta:
        db_table = 'users'
    
    # @property
    # def id(self):
    #     return self.user_id
    
    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['username'] 

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.first_name
        super().save(*args, **kwargs)



class roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name or f"Role {self.role_id}"
    class Meta:
        db_table = 'roles'

class permissions(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.permission_id or f"Role {self.permission_id}"
    class Meta:
        db_table = 'permissions'

