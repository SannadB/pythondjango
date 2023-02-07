from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Category, Product, Brand, Inventory

def myfunc(request):
    inventory = Inventory.objects.get(id=1)
    return HttpResponse(inventory)
