from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings

def home(request):
    return HttpResponse("hello")
