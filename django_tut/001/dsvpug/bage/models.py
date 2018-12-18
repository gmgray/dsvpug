from django.db import models
from datetime import datetime
# Create your models here.

class Status(models.Model):
    status      =   models.CharField(max_length=20,null=False,blank=False)
    descrption  =   models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.status
        

class Srq(models.Model):
    srqNo      =   models.IntegerField(blank=False,null=False,default=0)
    requestor   =   models.CharField(max_length=20)
    site        =   models.CharField(max_length=20)
    title       =   models.CharField(max_length = 200)
    description =   models.TextField()
    added       =   models.DateTimeField(default=datetime.now())
    status      =   models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return ("%s: %s" %(self.srqNo,self.title))
