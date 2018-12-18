from django import forms

from .models import Incident

class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ('author','title','email', 'description',)