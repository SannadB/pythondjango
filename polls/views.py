from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Category, Product, Brand, Inventory

def myfunc(request, id):
    return HttpResponse(id)
