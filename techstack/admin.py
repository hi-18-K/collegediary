# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Techstack, Tag, Nontech


admin.site.register(Techstack)
admin.site.register(Tag)
admin.site.register(Nontech)
