from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'aduh123jn512i'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thepassword = ''
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    numbers = list('0123456789')
    
    special = list("!@#$%^&*()")
    
    if request.GET.get('uppercase'):
        characters.extend(uppercase)
        
    if request.GET.get('numbers'):
        characters.extend(numbers)
    
    if request.GET.get('special'):
        characters.extend(special)
    
    length = int(request.GET.get('length', 12))
    
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': thepassword})