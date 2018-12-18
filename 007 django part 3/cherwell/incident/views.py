from django.shortcuts import render, get_object_or_404, redirect
from .models import Incident
from .forms import IncidentForm
from django.utils import timezone
# Create your views here.

def incidents(request):
    data=Incident.objects.all()
    return render(request,'incident/incidents.html',{'data':data})

# def incident_detail(request):
#     form=IncidentForm()
#     return render(request,'incident/detail.html',{'form':form})


def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == "POST":
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.author = request.user
            incident.published_date = timezone.now()
            incident.save()
            return redirect('incident_detail', pk=incident.pk)
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incident/detail.html', {'form': form})