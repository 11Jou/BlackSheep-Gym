from django.shortcuts import render
from django.http import HttpResponse
from .models import Msg , Coach

def index(request):
    trainer = Coach.objects.all()
    if (request.method == "POST"):
        name = request.POST.get('name')
        mail = request.POST.get('email')
        msg = request.POST.get('message')
        Data = Msg(name = name , mail = mail , message = msg)
        Data.save()
        return render(request, 'Home.html' , {'trainer':trainer})
    else:
        return render(request, 'Home.html', {'trainer':trainer})
