# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Product
from ..login_app.models import User
# Create your views here.
def home(request):
    context = {
        'cur_user': User.objects.get(id = request.session['id']),
        'user_products': Product.objects.filter(wishlist = request.session['id']),
        'other_products': Product.objects.exclude(wishlist = request.session['id']),
    }
    return render(request, 'list_app/home.html', context)

def addproduct(request):
    return render(request, 'list_app/add.html')

def show(request, id):
    context = {
        'item': Product.objects.get(id = id),
    }
    return render(request, 'list_app/show.html', context)

def create(request):
    logged_user = User.objects.get(id = request.session['id'])
    new_product = Product.objects.create(name = request.POST['product_name'], created_by = logged_user)
    logged_user.items_made.add(new_product)
    logged_user.wishlists.add(new_product)
    return redirect('/main/home')

def addtolist(request, id):
    item = Product.objects.get(id = id)
    user = User.objects.get(id = request.session['id'])
    user.wishlists.add(item)
    return redirect('/main/home')

def removefromlist(request, id):
    item = Product.objects.get(id = id)
    user = User.objects.get(id = request.session['id'])
    user.wishlists.remove(item)
    return redirect('/main/home')

def delete(request, id):
    item = Product.objects.get(id = id)
    item.delete()
    return redirect('/main/home')
    