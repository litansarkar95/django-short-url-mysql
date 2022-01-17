from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000,null=True,blank=True)
    uuid = models.CharField(max_length=10)
    create_date =models.DateTimeField(auto_now_add=True)
