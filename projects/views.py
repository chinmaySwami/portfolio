from django.shortcuts import render
from .models import Projects

# Create your views here.
def show(request):
    proj = Projects.objects
    return render(request, 'projects\projects.html', {'projs': proj})
