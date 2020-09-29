from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def filter_demo(request):
    return render(request,"filter_demo.html",{'data':"hello world",'a':20,'b':60,'num':5})