from rest_framework.viewsets import ModelViewSet

from resume_app.models import Resume
from resume_app.serializers import ResumeSerializer


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
