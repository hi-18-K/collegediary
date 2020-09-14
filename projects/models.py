# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from techstack.models import Techstack, Tag, Nontech
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 20, null = False, unique = True)
    detail = models.CharField(max_length = 150, null = False)
    githublink = models.URLField(max_length = 200)
    otherlink = models.URLField(max_length = 200)
    creator = models.ForeignKey('User', on_delete=models.CASCADE)
    tech = models.ManyToManyField('Techstack')
    tag = models.ManyToManyField('Tag')
