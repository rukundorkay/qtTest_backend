import uuid
from django.db import models
# from django.contrib.postgres.fields import ArrayField

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
    project_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # assignees = ArrayField(ArrayField(models.IntegerField()))

class Assignees(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name=name = models.CharField( ("name"),max_length=50,blank=False)
        
