from django.contrib import admin

# Register your models here.
from .models import Status,Incident

admin.site.register(Status)
admin.site.register(Incident)