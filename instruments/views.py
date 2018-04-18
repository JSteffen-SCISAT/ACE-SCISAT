from django.shortcuts import render_to_response
import os

# Create your views here.
def index(request):
	return render_to_response(os.path.join('instruments','index.html'))
	
def fts(request):
	return render_to_response(os.path.join('instruments','fts.html'))
	
def maestro(request):
	return render_to_response(os.path.join('instruments','maestro.html'))
	
def testing(request):
	return render_to_response(os.path.join('instruments','testing.html'))