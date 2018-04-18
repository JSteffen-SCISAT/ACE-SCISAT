from django.conf.urls import url
from . import views

app_name = 'mission'
urlpatterns = [
	url('launch/', views.launch, name='launch'),
	url('orbit/', views.orbit, name='orbit'),
	url('', views.index, name='index'),
]
