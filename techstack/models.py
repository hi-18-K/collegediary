# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Techstack(models.Model):                  # USE LIST SERCH METHOD
    tech = models.CharField(max_length = 50)

    def __str__(self):
        return self.tech



class Nontech(models.Model):                    # USE LIST SERCH METHOD
    fun = models.CharField(max_length = 50)

    def __str__(self):
        return self.fun



class Tag(models.Model):                        # USE SEARCH FILTER
    tag = models.CharField(max_length = 50)

    def __str__(self):
        return self.tag
