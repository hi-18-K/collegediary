from rest_framework import serializers
from .models import Project
from techstack.models import Techstack, Tag, Nontech
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
                    'id',
                    'title',
                    'detail',
                    'githublink',
                    'otherlink',
                    'creator',
                    'tech',
                    'tag'
                )
    #
    # def create(self):
    #     pass
