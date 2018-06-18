from django.db import models

# Create your models here.

class data(models.Model):
    file = models.FileField(default=None)
