'''
模型层，用于处理数据库相关的内容
'''

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class List(models.Model):
    id = models.AutoField(primary_key=True)

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    list_item = models.ForeignKey(List, default=None)
    text = models.TextField(default='')

