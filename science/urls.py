from django.urls import path
from . import views

app_name = 'science'
urlpatterns = [
    path('', views.index, name='index'),
	path('ozonedecline', views.ozonedecline, name='ozonedecline'),
    path('climatechange', views.climatechange, name='climatechange'),
    path('ozonemonitoring', views.ozonemonitoring, name='ozonemonitoring'),
    path('dataanalysis', views.dataanalysis, name='dataanalysis'),
    path('scienceresults', views.scienceresults, name='scienceresults'),
]
