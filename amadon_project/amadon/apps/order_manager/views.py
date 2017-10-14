# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    print "testing message"
    #return HttpResponse("This is an HttpResponse")
    return render(request, 'order_manager/index.html')

def back(request):
    return redirect('/')

def checkout(request):
    context = {
        'quantity':request.session['quantity'],
        'price':request.session['price'],
        'total':request.session['total']
    }
    return render(request, 'order_manager/checkout.html', context)


def item_1(request):
    print "someone tried to buy item_1"
    request.session['quantity'] = request.POST['quantity']
    print request.POST['product_id']
    if int(request.POST['product_id']) == 1:
        request.session['price'] = 20
    else:
        return HttpResponse("stop trying to hack my e-commerce site")
    request.session['total'] = int(request.session['price']) * int(request.POST['quantity'])
    context = {
        'quantity':request.session['quantity'],
        'price':request.session['price'],
        'total':request.session['total']
    }
    #return render(request, 'order_manager/checkout.html', context)
    return redirect('/gotocheckout', context)

def item_2(request):
    print "someone tried to buy item_2"
    request.session['quantity'] = request.POST['quantity']
    if int(request.POST['product_id']) == 2:
        request.session['price'] = 5
    else:
        return HttpResponse("stop trying to hack my e-commerce site")
    request.session['total'] = int(request.session['price']) * int(request.POST['quantity'])
    context = {
        'quantity':request.session['quantity'],
        'price':request.session['price'],
        'total':request.session['total']
    }
    #return HttpResponse("You tried to buy item_2")
    #return render(request, 'order_manager/checkout.html', context)
    return redirect('/gotocheckout', context)

def item_3(request):
    print "someone tried to buy item_3"
    request.session['quantity'] = request.POST['quantity']
    if int(request.POST['product_id']) == 3:
        request.session['price'] = 2
    else:
        return HttpResponse("stop trying to hack my e-commerce site")
    request.session['total'] = int(request.session['price']) * int(request.POST['quantity'])
    context = {
        'quantity':request.session['quantity'],
        'price':request.session['price'],
        'total':request.session['total']
    }
    #return HttpResponse("You tried to buy item_3")
    #return render(request, 'order_manager/checkout.html', context)
    return redirect('/gotocheckout', context)

def item_4(request):
    print "someone tried to buy item_4"
    request.session['quantity'] = request.POST['quantity']
    if int(request.POST['product_id']) == 4:
        request.session['price'] = 200
    else:
        return HttpResponse("stop trying to hack my e-commerce site")
    request.session['total'] = int(request.session['price']) * int(request.POST['quantity'])
    context = {
        'quantity':request.session['quantity'],
        'price':request.session['price'],
        'total':request.session['total']
    }
    #return HttpResponse("You tried to buy item_4")
    #return render(request, 'order_manager/checkout.html', context)
    return redirect('/gotocheckout', context)


