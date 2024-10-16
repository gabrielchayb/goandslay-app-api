"""
URL mappings for the user API.
"""
from django.urls import path
from user import views
from django.urls import path, include
from . import views 

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('logout/', views.logout.as_view(), name='logout'),
]