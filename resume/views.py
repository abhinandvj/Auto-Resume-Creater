from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume


# Create your views here.
def id1(request):
    ab = Resume.objects.get(id=1)
    return render(request,'home.html',{'ab':ab})

def id2(request):
    ab = Resume.objects.get(id=1)
    return render(request,'index.html',{'ab':ab})