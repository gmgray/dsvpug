# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Incident(models.Model):
    #incident_id = models.AutoField(primary_key=True)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    title  = models.CharField( max_length=50,blank=False,null=False)
    email  = models.EmailField( max_length=254,default='me@here.com')
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return("%s:%s"%(self.id,self.title))
