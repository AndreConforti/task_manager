from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('log_in', views.log_in, name='log_in'),
    path('register/', views.register, name='register'),
]
