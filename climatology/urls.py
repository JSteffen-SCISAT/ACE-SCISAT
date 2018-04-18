from django.urls import path

# imports for static urls
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'climatology'
urlpatterns = [
    path('', views.index, name='index'),
	path('climatology35', views.climatology35, name='climatology35'),
	path('climatology22', views.climatology22, name='climatology22'),
	path('climatology22NOy', views.climatology22NOy, name='climatology22NOy'),
]
