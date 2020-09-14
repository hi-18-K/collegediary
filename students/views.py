from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
# from .forms import UserForm
# from collegediary.decorators import admin_hr_required, admin_only
from .serializers import StudentSerializer, LoginSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication


class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer


# class SingleStudentProfile():
#     pass
#
# class MyProfile():
#     pass


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data =request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data("user")
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key}, status =200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def post(self, request):
        logout(request)
        return Response(status =204)
