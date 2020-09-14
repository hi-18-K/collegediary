# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from techstack.models import Techstack, Nontech
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Techintrst = models.ManyToManyField('techstack.Techstack')
    Nontechintrst = models.ManyToManyField('techstack.Nontech')
