from django.shortcuts import render

def index(request):
    return render(request, 'theme/home.html')

def acknowledgment(request):
    return render(request, 'theme/acknowledgment.html')