import uuid
from django.db import models

# Create your models here.
class Task(models.Model):
    Priority_CHOICES = (
        ('LOW', 'LOW'),
        ('NORMAL', 'NORMAL'),
        ('HIGH', 'HIGH'),
        )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( ("name"),max_length=50,blank=False)
    start_date=models.DateField(("start date"),blank=False)
    end_date=models.DateField(("end date"),blank=False)
    description=models.CharField(("description"),max_length=100,blank=False)
    priority= models.CharField(("priority"),max_length=40,choices=Priority_CHOICES, default='LOW'),
    file_attachment=models.CharField(("file attachment"),blank=False,max_length=100)
