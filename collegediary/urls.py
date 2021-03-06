"""collegediary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from students.views import (LoginView, LogoutView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('api/projects/', include('projects.api_urls')),

    path('students/', include('students.urls')),
    path('api/students/', include('students.api_urls')),

    path('blog/', include('blog.urls')),
    path('api/blog/', include('blog.api_urls')),

    # path('techstack/', include('techstack.urls')),
    # path('api/techstack/', include('techstack.api_urls')),

    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/login/', LoginView.as_view()),
    path('api/auth/logout/', LogoutView.as_view()),
]
