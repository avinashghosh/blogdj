from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
