from django.urls import path
from user.views import *

urlpatterns = [
    path('', UserList, name='user-list'),
    path('details/<int:id>/', UserDetails, name='user-details'),
    path('edit/<int:id>/', UserEdit, name='user-edit'),
    path('add/', UserAdd, name='user-add'),
    path('delete/<int:id>/', UserDelete, name='user-delete'),


]