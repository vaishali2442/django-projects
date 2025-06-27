from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser),
    path('roles/create/', views.createRole, name='create_role'),
    path('roles/update/', views.updateRole, name='update_role'),
    path('roles/', views.getRole, name='get_role'),
    path('roles/delete/', views.deleteRole, name='delete_role'),

    path('users/create/', views.createUser, name='create_user'),
    path('users/update/', views.updateUsers, name='update_user'),
    path('users/', views.getUsers, name='get_users'),
    path('users/delete/', views.deleteUser, name='delete_user'),
    path('users/map-user/', views.mapUser, name='map_user'),

    path('permissions/create/', views.createPermissions, name='create_permissions'),
    path('permissions/update/', views.updatePermissions, name='update_permissions'),
    path('permissions/', views.getPermissions, name='get_permissions'),
    path('permissions/delete/', views.deletePermissions, name='delete_permissions')



]
