"""
URL configuration for adminmm app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('adminmm/', views.admin_home, name="admin_home"),
    path('addmentor/', views.add_mentor, name="add_mentor"),
    path('update_mentor/', views.update_mentor_details, name="update_mentor_details" ),
    path('mentor_details/', views.show_mentor_details, name="show_mentor_details"),
    path('mentee_details/', views.view_mentee_details, name="view_mentee_details"),
    path('overall_report/', views.overall_report, name="overall_report"),
    path('delete_mentor/', views.delete_mentor, name="delete_mentor"),
]
