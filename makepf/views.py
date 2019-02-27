from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def ShowPortfolio(request):
    portfolio = Portfolio.objects
    return render(request, 'ShowPortfolio.html', {'portfolios': portfolio})

def add(request):
    return render(request,'add.html')
