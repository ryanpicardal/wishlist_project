# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    created_by = models.ForeignKey(User, related_name='items_made')
    wishlist = models.ManyToManyField(User, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    