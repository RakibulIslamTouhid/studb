from django.shortcuts import render

# Create your views here.
from .models import Info

def home(request):
    infos = Info.objects
    return render(request,'info/home.html', {'infos':infos})