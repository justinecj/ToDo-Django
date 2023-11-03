from django.db import models
from datetime import date

# Create your models here.
class Entity(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.name
