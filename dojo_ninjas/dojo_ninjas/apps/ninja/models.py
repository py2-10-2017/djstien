# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#class Blog(models.Model):
      #name = models.CharField(max_length=255)
      #desc = models.TextField()
      #created_at = models.DateTimeField(auto_now_add = True)
      #updated_at = models.DateTimeField(auto_now = True)

#class Comment(models.Model):
      #comment = models.CharField(max_length=255)
      #created_at = models.DateTimeField(auto_now_add = True)
      #updated_at = models.DateTimeField(auto_now = True)
      # Notice the association made with ForeignKey for a one-to-many relationship
      # There can be many comments to one blog
      #blog = models.ForeignKey(Blog, related_name = "comments")

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojos, related_name = "ninjas")
    desc = models.TextField(blank=True, null=True)

