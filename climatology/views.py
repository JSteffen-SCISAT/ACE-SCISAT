from django.shortcuts import render, render_to_response
import os

################################
# Create your views here.

def index(request):
    return render_to_response(os.path.join('climatology','index.html'))
	
def climatology22(request):
    return render_to_response(os.path.join('climatology','climatology22.html'))
	
def climatology22NOy(request):
    return render_to_response(os.path.join('climatology','climatology22NOy.html'))
	
def climatology35(request):
    return render_to_response(os.path.join('climatology','climatology35.html'))


