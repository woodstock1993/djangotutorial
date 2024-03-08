from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_user, name='register'),
    path('registers/', RegisterAPI.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),    
]