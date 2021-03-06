from django.contrib import admin
from django.urls import path, include

from dashboard import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', views.login, name='backstage'),
    path('api/v1/', include('examapi.urls')),
    path('exam/', include('exam.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('account.urls')),
]
