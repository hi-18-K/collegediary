from rest_framework import serializers
from django.contrib.auth.models import User


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = (
                'id',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'url'
        )
