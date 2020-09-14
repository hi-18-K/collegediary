# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{suthor_id}/{title}-{filename}'.format(
            author_id =str(instance.author.id), title =str(instance.title), filename =filename
    )
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length =50, null =False, blank =False)
    body = models.TextField(max_length =50, null =False, blank =False)
    date_published = models.DateTimeField(auto_now_add=True, verbose name = "date published")
    date_updated = models.DateTimeField(auto_now_add=True, verbose name = "date updated")
    author = models.ForeignKey(on_delete = models.CASCADE)
    slug = models.SlugField(blank =True, unique =True)

    def __str__(self):
        return self.title

    def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.author.username + "-" +instance.title)

    pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)
