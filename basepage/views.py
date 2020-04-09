from django.shortcuts import render
from django.http import HttpResponse
from .models import description

# Create your views here.

def homepage(request):
    return render(request = request,
                   template_name="basepage/home.html",
                   context ={"descriptions": description.objects.all})
