from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a=7+8
    return  render(request,'about.html',{'get':a})

def home(request):
    return HttpResponse('This is my home')