from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('log_in/', views.log_in, name='log_in'),
    path('register/', views.register, name='register'),
    path('log_out/', views.log_out, name='log_out'),
    path('activate_account/<str:token>/', views.activate_account, name='activate_account'),
]
