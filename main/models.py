from __future__ import unicode_literals
from django.db import models
from django import forms

# Create your models here.

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    message = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to ='')
    uploaded_at = models.DateTimeField(auto_now_add=True)