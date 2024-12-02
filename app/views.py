from django.shortcuts import render
from django.http import HttpResponse
from .models import product

# Create your views here.
def index(request):
    context = {}
    return render(request, 'app/home.html',context)
def cart(request):
    context = {}
    return render(request, 'app/cart.html', context)
def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)

