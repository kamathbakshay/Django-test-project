from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
   return render(request, "myapp/template/myapp/hello.html", {})

def hello2(request):
   return HttpResponse('index hello')

def hello3(request):
   return render(request, "myapp/hello.html", {})