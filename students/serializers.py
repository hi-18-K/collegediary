from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import exceptions
from django.contrib.auth import authenticate


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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "Your account is deactivated!"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Please check your credentials!"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide Username and Password both"
            raise exceptions.ValidationError(msg)
        return data
