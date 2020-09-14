# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student
from rest_framework.authtoken.admin import TokenAdmin


admin.site.register(Student)

TokenAdmin.raw_id_fields = ['user']
