from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio


# Create your views here.
def id1(request):
    ab = Portfolio.objects.get(id=1)
    return render(request,'index.html',{'ab':ab})

def id2(request):
    ab = Portfolio.objects.all()
    return render(request,'index.html',{'ab':ab})