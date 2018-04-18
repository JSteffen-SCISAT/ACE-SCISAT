from django.urls import path

from . import views

app_name = 'montreal'
urlpatterns = [
    path('', views.index, name='index')
]
