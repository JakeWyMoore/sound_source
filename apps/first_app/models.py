from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
  def basic_validator(self, postData):
    errors = {  }

    # Email Validations
    email = postData['email']
    if '@' not in email:
      errors['email'] = "Invalid Email"
    if '.' not in email:
      errors['email'] = "Invalid Email"

    # Password Validations
    if len(postData['password']) < 8:
      errors['password'] = "Password must be 8 characters or more."
    
    # Nickname Validations
    if len(postData['nickname']) < 1:
      errors['nickname'] = "Nickname must be provided."

    return errors

class User(models.Model):
  email = models.CharField(max_length = 50)
  password = models.CharField(max_length = 25)
  nickname = models.CharField(max_length = 25)
  image = models.ImageField(default='default.png', blank = True)
  objects = UserManager()