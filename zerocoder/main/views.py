from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello. перейди data или test</h1>")

def data(request):
    return HttpResponse("<h1>Это старница DATA</h1>")

def test(request):
    return HttpResponse("<h1>Это страница TEST</h1>")