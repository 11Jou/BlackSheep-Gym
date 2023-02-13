from django.shortcuts import render
from django.http import HttpResponse
from .models import Offer

def offer(request):
    data = Offer.objects.all()
    return render(request, 'offers.html', {'offer':data})