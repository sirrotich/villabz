from django.shortcuts import render,redirect
from django.http  import JsonResponse, HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'index.html')
