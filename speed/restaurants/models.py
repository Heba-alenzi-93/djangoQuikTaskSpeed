from datetime import datetime
from django.db import models

# Create your models here.

class Restaurant(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()
    opening_time = models.DateField()
    closing_time= models.DateField()
    created_at = models.DateField(auto_now_add=True)

