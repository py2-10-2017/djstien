# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
# the index function is called when root is visited

def index(request):
    response = "Welcome"
    print response
    return render(request, "random_word/index.html")

def getword(request):
    request.session['myword'] = get_random_string(length=14)
    # wordgen = get_random_string(length=14)
    # print wordgen
    return render(request, "random_word/getword.html")
