from django.urls import path, include
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.show, name='show')
]