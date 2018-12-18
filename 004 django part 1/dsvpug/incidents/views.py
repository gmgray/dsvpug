from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

a={
    "Imie" : "Dupa",
    "Nazwisko" : "Cycki",
}

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def json(request):
    return JsonResponse(a)