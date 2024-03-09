from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.main, name='main'),
    path('user_info/', views.user_info, name='user_info'),
]