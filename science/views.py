from django.shortcuts import render_to_response
import os

# Create your views here.

def index(request):
	return render_to_response(os.path.join('science','index.html'))
	
def ozonedecline(request):
	return render_to_response(os.path.join('science','ozonedecline.html'))
	
def climatechange(request):
	return render_to_response(os.path.join('science','climatechange.html'))
	
def ozonemonitoring(request):
	return render_to_response(os.path.join('science','ozonemonitoring.html'))
	
def dataanalysis(request):
	return render_to_response(os.path.join('science','dataanalysis.html'))
	
def scienceresults(request):
	return render_to_response(os.path.join('science','scienceresults.html'))