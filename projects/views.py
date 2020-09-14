from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.db.models import Q

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import action

# from collegediary.decorators import admin_hr_required, admin_only
# from projects.forms import ProjectForm, ChoiceForm
from projects.models import *
from projects.serializers import ProjectSerializer# , ChoiceSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters


@csrf_exempt
def project(request):
    if request.method == "GET":
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many = True, context={'request': request})
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        jsondata = JSONParser()
        data = jsondata.parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def project_details(request, id):
    try:
        instance = Project.objects.get(id=id)
    except Project.DoesNotExist as e:
        return JsonResponse({"error": "Given project instance not found"}, status =404)

    if request.method == "GET":
        serializer = ProjectSerializer(instance)
        return JsonResponse(serializer.data, safe = True)

    elif request.method == "PUT":
        jsondata = JSONParser()
        data = jsondata.parse(request)
        serializer = ProjectSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        instance.delete()
        return HttpResponse(status =204)
