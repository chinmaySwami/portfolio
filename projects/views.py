from django.shortcuts import render
from .models import Projects

# Create your views here.
def show(request):
    proj = Projects.objects
    return render(request, template_name='projects/base.html', context={'projs': proj})
