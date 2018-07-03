from django.shortcuts import render
from .models import Post
from django.template import Context, loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response

def home(request):
    return render(request, 'main/home.html')
   
def about(request):
    return render(request, 'main/about.html')
    
def books(request):
    return render(request, 'main/books.html')
    
def single(request):
    return render(request, 'main/single.html')
    


