from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the test index.")

def alf(request):
    return HttpResponse("Hello, alf.")

def detail(request, yv_id):
    tags = Tag.objects.order_by('tag')[:yv_id]
    output = ', '.join([t.tag for t in tags])
    return HttpResponse(output)
