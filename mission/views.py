from django.shortcuts import render, render_to_response
import os

# Create your views here.
def index(request):
    return render_to_response(os.path.join('mission','index.html'))
	
def orbit(request):
    return render_to_response(os.path.join('mission','orbit.html'))
	
def launch(request):
    return render_to_response(os.path.join('mission','launch.html'))