from django.shortcuts import render_to_response
import os

# Create your views here.
app_name = 'atlases'
def solar(request):
	return render_to_response(os.path.join('atlases','solaratlas.html'))
	
def ace(request):
	return render_to_response(os.path.join('atlases','aceatlas.html'))