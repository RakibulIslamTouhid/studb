from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Info

def home(request):
    infos = Info.objects
    return render(request,'info/home.html', {'infos':infos})

def entry(request):
    if request.method=='POST':
        if request.POST['name'] and  request.POST['roll'] and request.POST['dept'] and  request.POST['section'] and  request.POST['blood']  and request.FILES['image']:
            entry = Info()
            entry.name = request.POST['name']
            entry.roll = request.POST['roll']
            entry.dept = request.POST['dept']
            entry.section = request.POST['section']
            entry.blood = request.POST['blood']
            entry.image = request.FILES['image']
            
            
            entry.save()
            return redirect('home')


        else:
            return render(request,'info/entry.html',{'error':' All fields are required' })


    else:
        return render(request,'info/entry.html')
