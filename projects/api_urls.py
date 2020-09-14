from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from .import views as projectView

urlpatterns = [
    # path('', projectView.project, name = 'project-home'),
    # path('<int:id>/', projectView.project_details, name = 'project-detail'),
    # path('', projectView.ProjectAPIView.as_view(), name = 'project-home'),
    # path('<int:id>/', projectView.ProjectDetailAPIView.as_view(), name = 'project-detail'),
    path('generics/', projectView.ProjectListView.as_view(), name = 'project-home'),
    path('generics/<int:id>/', projectView.ProjectListView.as_view(), name = 'project-detail'),
]
