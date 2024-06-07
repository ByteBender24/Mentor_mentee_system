"""
URL configuration for mentor app.

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
    path('mentor/', views.mentor_home, name="mentor_home"),
    path('addmentee/', views.add_mentee, name="add_mentee"),
    path('update_mentor_details/', views.update_mentor_details, name="update_mentor_details"),
    path('show_mentor_details/', views.show_mentor_details, name="show_mentor_details"),
    path('show_mentee_details/', views.show_mentee_details, name="show_mentee_details"),
    path('SearchMentees/', views.search_mentee, name="search_mentee"),
    path('editmentee/', views.update_mentee_details, name="update_mentee_details"),
    path('meetings/', views.add_meeting, name="add_meeting"),
    path('search_meeting/', views.search_meeting, name="search_meeting"),
    path('list_of_mentees/', views.list_of_mentees, name="list_of_mentees"),
    path('meeting_requests_mentor/', views.mentor_meeting_request, name="mentor_meeting_request"),
    path('deletementee/', views.delete_mentee, name="delete_mentee"),
    path('announcements/', views.announcement_mentor, name="announcement_mentor"),
    path('update_marks/', views.update_mentee_marks, name="update_mentee_marks"),
    path('showmarks/', views.show_mentee_marks, name="show_mentee_marks"),
]
