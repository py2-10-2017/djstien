# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate_registration(self, form_data):
        errors = []

        if len(form_data["first_name"]) < 2:
            errors.append("First Name must be at least two characters")
        if len(form_data["last_name"]) < 2:
            errors.append("Last Name must be at least two characters")
        if len(form_data["password"]) == 0:
            errors.append("Must enter a password")
        if len(form_data["password"]) < 8:
            errors.append("Password must be at least 8 characters")
        if form_data["password"] != form_data["confirm_pw"]:
            errors.append("Passwords do not match")
        #if User.objects.get(email=form_data['email']):
            #errors.append('Email is already registered.')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
