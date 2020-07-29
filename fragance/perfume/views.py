from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

def index(request):
    context = {} 
    return render(request, 'perfume/index.html', context)


