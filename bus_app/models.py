from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager

# Create your models here.


class BusStop(gismodels.Model):
    name = models.TextField()
    geom = gismodels.PointField()
    objects = GeoManager()

    def __unicode__(self):
        return self.name
