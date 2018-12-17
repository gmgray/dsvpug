from django.db import models
from django.utils import timezone

# Create your models here.
class Incident(models.Model):
    #incident_id = models.AutoField(primary_key=True)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    title  = models.CharField( max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        """This one will be used in forms,
        so we can call Incident.save() after updating form fields easily"""
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        """This return object representation as a string"""
        return ("%s : %s" % (self.id, self.title))

    class Meta:
        """Here are some meta data which will be useful for displaying model.
        verbose_name is model's name displayed
        verbose_name_plural is name displayed for plural form."""
        verbose_name = "Incident"
        verbose_name_plural = "Incidents"

