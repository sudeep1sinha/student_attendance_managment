import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#from student_management_app.EmailBackEnd import EmailBackEnd

from django.shortcuts import render

# Create your views here.
def showDemoPage(request):
    return render(request,"login.html")

