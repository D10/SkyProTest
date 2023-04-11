from django.urls import path
from rest_framework.routers import SimpleRouter

from resume_app.views import ResumeViewSet

urlpatterns = [
    path('resume/<int:pk>/', ResumeViewSet.as_view({'get': 'list', 'patch': 'partial_update'}))
]
