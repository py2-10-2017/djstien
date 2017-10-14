# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    print "Hi"
    return render(request, 'surveyform/index.html')

def process(request):
    print "Submit"
    print request.POST["name"]
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']   
    #return render(request, 'surveyform/results.html')
    return redirect('/survey/submit_data')

def submit(request):
    print request.session
    context = {
        'name':request.session['name'],
        'location':request.session['location'],
        'language':request.session['language']
    }
    #return HttpResponse("something")
    return render(request, 'surveyform/results.html', context)