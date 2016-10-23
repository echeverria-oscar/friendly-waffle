from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):
    def login(self, post):
        user_list = User.objects.filter(username = post['username'])
        if user_list:
            user = user_list[0]
            if bcrypt.hashpw(post['password'].encode(), user.password.encode()) == user.password:

                return user
        return None

    def register(self, post):
        encrypted_password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
        User.objects.create(name = post['name'], username = post['username'], password = encrypted_password)

    def validate(self, post):
        errors = []

        if len(post['name']) == 0:
            errors.append("Name is required")

        if len(post['username']) == 0:
            errors.append("Username is required")


        if len(post['password']) == 0:
            errors.append("must enter a password")
        elif len(post['password']) < 8:
            errors.append("password must have at least 8 characters")
        elif post['password'] != post['confirm_pass']:
            errors.append("password and confirmation must match")

        if len(User.objects.filter(username = post['username'])) > 0 :
            errors.append("Username is unavailable!")

        return errors

class TripManager(models.Manager):
    def maketrip(self, post):
        errors = []

        if len(post['destination']) == 0:
            errors.append("Destination is required")
        if len(post['description']) == 0:
            errors.append("Description is required")
        if len(post['travel_from']) == 0:
            errors.append("Travel Start Date is required")
        if len(post['travel_to']) == 0:
            errors.append("Travel End Date is required")


        return errors

class User(models.Model):
    name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 45)
    password = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    travel_from = models.DateTimeField()
    travel_to = models.DateTimeField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
