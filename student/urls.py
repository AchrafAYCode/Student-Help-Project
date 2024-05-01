from django.urls import path ,include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list/', views.index, name='list'),
    path('logout/',auth_views.LogoutView.as_view(template_name='student/registration/logout.html'), name ='logout'),
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
   
]