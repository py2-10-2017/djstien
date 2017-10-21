# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Course

# Create your views here.

def index(request):
    #return HttpResponse('Page Loaded')
    print Course.__doc__
    #Course.objects.create(title="Creative Writing", description="How to write creatively and probably other things too")
    courses = Course.objects.all()
    context = {
        "course_list" : courses 
    }
    return render(request, "courses/index.html", context)

def addclass(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        print "validation fail"
        print errors
        courses = Course.objects.all()
        context = {
            "title" : errors,
            "course_list" : courses
        }
        return render(request, "courses/index.html", context)
    else:
        print "adding a course to the table, boss"
        Course.objects.create(title=request.POST["title"], description=request.POST["description"])
        return redirect('/')

def removecourse(request, id):
    coursedel = Course.objects.get(id=request.POST["removeid"])
    context = {
        "rem_course" : coursedel
    }
    return render(request, 'courses/remove.html', context)

def destroy(request):
    print "removing a course here, boss"
    delcourse = Course.objects.get(id=request.POST["remid"])
    delcourse.delete()
    return redirect('/')
    

