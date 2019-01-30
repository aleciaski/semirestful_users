from __future__ import unicode_literals

from django.db import models
import re

class UserManager(models.Manager):
    def custom_basic_validator(self, user_data):
        errors = {}
        if len(user_data["first_name"]) < 1:
            errors["error_first_name"] = "Please enter your first name."
        if len(user_data["last_name"]) < 1:
            errors["error_last_name"] = "Please enter your last name."
        if len(user_data["email"]) < 1:
            errors["error_email"] = "Please enter your email address"
        elif not re.compile(r'[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9]+').match(user_data["email"]):
            errors["error_email"] = "Invalid email format"
        return errors

class User(models.Model):
	first_name= models.CharField(max_length= 255)
	last_name= models.CharField(max_length= 255)
	email= models.EmailField()
	created_at= models.DateTimeField(auto_now_add=True)
    objects= UserManager()


def __unicode__(self):
        return "id : " + str(self.id) + ", first_name : " + self.first_name + ", last_name : " + self.last_name + ", email : " + self.email + ", created_at : " + str(self.created_at)
	# objects= CustomManager()
# Create your models here.
