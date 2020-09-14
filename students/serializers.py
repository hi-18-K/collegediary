from rest_framework import serializers
from django.db.models import User


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
                'id',
                'first_name',
                'last_name',
                'email',
                'url'
        )
