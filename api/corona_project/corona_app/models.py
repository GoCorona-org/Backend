from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.
#"UUID","Status","Lat","Lng"

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class CoronaApp(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, blank=True, default='a')
    status = models.IntegerField(default=0)
    
    latitude= models.FloatField(default=0)
    longitude= models.FloatField(default=0)



    class Meta:
        ordering = ['created']


# class PositionData(models.Model):
#     created = models.DateTimeField(auto_now_add=True)

#     name = models.CharField(max_length=100, blank=True, default='a')
#     status = models.IntegerField(default=0)
