"""
URL configuration for student_attendance_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from student_management_app import views

from student_management_app import models
urlpatterns = [
    
    path('login/',views.showDemoPage),
    path('admin/',admin.site.urls),
    
    path('api/login/', views.LoginAPIView.as_view(),name='api-login'),
    
    #below tum Aage bana sakta hai 
    
    #  path('api/logout/', views.LogoutAPIView.as_view(), name='api-logout'),
    # path('api/register/', views.RegisterAPIView.as_view(), name='api-register'),
]
