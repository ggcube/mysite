from django.shortcuts import render


def home(request):
    PP = map(str,range(100))
    return render(request, 'home.html', {'PP':PP})


# Create your views here.
