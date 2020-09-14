from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
# from .forms import UserForm
# from collegediary.decorators import admin_hr_required, admin_only
from .serializers import StudentSerializer

from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer
