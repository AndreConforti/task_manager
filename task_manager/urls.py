from django.contrib import admin
from django.urls import path, include
from account.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('account/', include('account.urls')),
    path('report/', include('report.urls')),
]
