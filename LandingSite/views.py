from django.shortcuts import render
from django.http      import HttpResponse


# Create your views here.
def index(request):
    return render(request,'Home.html')

def products(request):
    return render(request,'Products.html')

def resources(request):
    return render(request,'resources.html')

