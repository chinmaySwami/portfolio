from django.urls import path, include
from . import views

app_name = 'basepage'

urlpatterns = [
    path("", views.homepage, name="homepage")
]