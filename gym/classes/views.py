from django.shortcuts import render
from django.http import HttpResponse

def classes(request):
    return render(request , 'class.html')