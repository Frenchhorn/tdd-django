from django.db import models

# Create your models here.
class List(models.Model):
    id = models.AutoField(primary_key=True)

class Item(models.Model):
    list_item = models.ForeignKey(List, default=None)
    text = models.TextField(default='')

