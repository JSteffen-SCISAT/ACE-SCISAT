from django.urls import path

# imports for static urls
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'scenario'
urlpatterns = [
    path('', views.index, name='index'),
]
