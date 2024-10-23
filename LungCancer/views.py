# only to display text
# from django.http import HttpResponse

# def about(request):
#     return HttpResponse("welcome to mysql")

from django.shortcuts import render

def home(request): 
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def pridict(request):
    return render(request,"pridict.html")

def result(request):
    return render(request,"result.html")

