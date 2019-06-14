from django.urls import path
from . import views

from djgeojson.views import GeoJSONLayerView




urlpatterns = [
    path('', views.index, name='index')
]
