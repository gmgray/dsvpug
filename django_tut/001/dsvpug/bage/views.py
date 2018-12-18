from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def getdate(request):    
    resp="""
    <html>
    <head>
    </head>
    <body>
    <h1>
    Today is %s 
    </h1>
    </body>
    </html>""" % datetime.now()
    return HttpResponse(resp)


def cokolwiek(request):
    resp = {
        "response":"current_date",
        "value":datetime.now()
    }
    return JsonResponse(resp)