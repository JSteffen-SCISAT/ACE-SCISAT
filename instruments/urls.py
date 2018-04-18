from django.urls import path

# imports for static urls
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'instruments'
urlpatterns = [
    path('', views.index, name='index'),
	path('fts', views.fts, name='fts'),
	path('maestro', views. maestro, name='maestro'),
	path('testing', views.testing, name='testing'),
]
