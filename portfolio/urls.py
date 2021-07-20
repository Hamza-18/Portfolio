from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:proj_name>', views.project, name='project')
]