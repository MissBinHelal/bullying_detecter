from django.shortcuts import render , redirect 
#from django.contrib import messages
#from .models import names
#import re
# Create your views here.

def index(request):
    return render(request, "bully_detect_app/startbootstrap-stylish-portfolio-gh-pages/index.html")
