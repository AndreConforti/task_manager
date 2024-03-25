from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('etl/', views.etl, name='etl')
]
