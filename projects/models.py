# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from techstack.models import Techstack, Tag, Nontech
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 20, null = False, unique = True)
    detail = models.CharField(max_length = 150, null = False)
    datepub = models.DateTimeField(auto_now_add=True, verbose name = "date published")
    githublink = models.URLField(max_length = 200)
    otherlink = models.URLField(max_length = 200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tech = models.ManyToManyField('techstack.Techstack', null = False)
    tag = models.ManyToManyField('techstack.Tag')

    def __str__(self):
        return self.title
