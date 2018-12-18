from django.db import models
from datetime import datetime

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=20,null=False,blank=False)
    description = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.status

class Incident(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    status = models.ForeignKey('Status',on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=datetime.now)
    
    
    def __str__(self):
        return self.title