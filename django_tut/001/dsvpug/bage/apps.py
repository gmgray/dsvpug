from django.contrib import admin
from django.apps import AppConfig
from bage.models import Srq, Status

admin.site.register(Srq,Status)

class BageConfig(AppConfig):
    name = 'bage'
