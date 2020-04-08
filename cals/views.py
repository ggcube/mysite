from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponseRedirect( reverse('add2',args=(a,b)))

def add2(request,a,b):
    c = int(a) + int(b)
    ans = str(a)+"+"+str(b)+"="+str(c)
    return HttpResponse(ans)

def index(request):
    return HttpResponse(request,'home.html')



# Create your views here.
