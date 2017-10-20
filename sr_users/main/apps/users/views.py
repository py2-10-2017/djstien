# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Person
# Create your views here.

def index(request):
    print "Welcome to Semirestful Users!"
    print Person.__doc__
    #Person.objects.create(name="Craig Biggio", email="cbigs@gmail.com")
    people = Person.objects.all()
    context = {
        "all_people" : people 
    }
    return render(request, 'users/index.html', context) 

def addform(request):
    print "running addform"
    return render(request, 'users/addform.html')

def create(request):
    Person.objects.create(name=request.POST["name"], email=request.POST["email"])
    print "User made"
    return redirect('/users')

def update(request):
    updateuser = Person.objects.get(id=request.POST["editid"])
    context = {
        "userupdate" : updateuser
    }
    return render(request, 'users/update.html', context)
    

def getperson(request, id):
    context = {
        "show_user": Person.objects.get(id=id)
    }
    return render(request, 'users/show.html', context)

def changeuser(request):
    userchange = Person.objects.get(id=request.POST["id"])
    userchange.name = request.POST["new name"]
    userchange.email = request.POST["new email"]
    userchange.save()
    return redirect ('/users')
    



