# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from models import User
import bcrypt

# Create your views here.
def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)


def index(request):
    print User.__doc__
    users = User.objects.all()
    context = {
        "users_list" : users
    }
    #print users
    return render(request, 'login/index.html', context)

def useradd(request):
    if request.method == "POST":
        errors = User.objects.validate_registration(request.POST)
        if not errors:
            print "forms looks ok"
            hash_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=hash_pw)
            context = {
                "regis_user" : user
            }
            return render(request, "login/success.html", context)
        else: 
            flash_errors(errors, request)
            print "trying to flash errors"
            return redirect('/')

def userlogin(request):
    print "someone tried to log into their account"
    email_query = User.objects.get(email=request.POST["email"])
    if email_query == "": 
        messages.error(request, "email not registered")
        return redirect('/')
    elif not bcrypt.checkpw(request.POST["password"].encode(), User.objects.get(email=email_query.email).password.encode()):
        messages.error(request, "wrong password")
        return redirect('/')
    elif bcrypt.checkpw(request.POST["password"].encode(), User.objects.get(email=email_query.email).password.encode()):
        user = User.objects.get(email=email_query.email)
        context = {
            "logged_user" : user
        }
        return render(request, 'login/success.html', context)
    else:
        return HttpResponse("There was a problem with your email/password. Please go back and try again")