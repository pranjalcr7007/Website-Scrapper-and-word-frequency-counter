from django.db import models

class data(models.Model):
    url = models.CharField(max_length=200)
    html = models.CharField(max_length=99999999)

   
    