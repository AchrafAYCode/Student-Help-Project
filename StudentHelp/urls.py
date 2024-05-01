"""
URL configuration for StudentHelp project.

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
from django.urls import path ,include 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='student/registration/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='student/registration/logout.html'), name ='logout'),
    
    path('accounts/', include('django.contrib.auth.urls')),
]