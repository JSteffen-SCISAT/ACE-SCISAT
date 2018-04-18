from django.urls import path

# imports for static urls
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'atlases'
urlpatterns = [
    path('ace_atlas/', views.ace, name='ace'),
	path('solar_atlas/', views.solar, name='solar'),
]
