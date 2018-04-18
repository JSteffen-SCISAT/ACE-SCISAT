from django.urls import path

# imports for static urls
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'molecules'
urlpatterns = [
    path('', views.index, name='index'),
    path('molecules35', views.molecules35, name='molecules35'),
    path('molecules30', views.molecules30, name='molecules30'),
    path('molecules22', views.molecules22, name='molecules22'),
    path('validation_O3', views.validation_O3, name='validation_O3'),
	#path('<slug:molecule>', views.index, name='index'),
]