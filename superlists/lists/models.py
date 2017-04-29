from django.db import models

# Create your models here.
class List(models.Model):
    pass

class Item(models.Model):
    list = models.ForeignKey(List, default=None)
    text = models.TextField(default='')

