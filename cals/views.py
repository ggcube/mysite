from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    ans = a+"+"+b+"="+str(c)
    return HttpResponse(ans)

def add2(request,a,b):
    c = int(a) + int(b)
    ans = str(a)+"+"+str(b)+"="+str(c)
    return HttpResponse(ans)

# Create your views here.
