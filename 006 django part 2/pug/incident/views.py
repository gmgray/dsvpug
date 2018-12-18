from django.shortcuts import render
from django.http import HttpResponse,request
from django.utils import timezone
from .models import Incident
# Create your views here.

def index(request):
    return HttpResponse("<h1>This is Incident landing page")

def incident_list(request):
    incidents = Incident.objects.all().order_by('published_date')
    #.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'incident/incident_list.html', {'incidents': incidents})