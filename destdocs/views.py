# coding: utf-8

from rest_framework import viewsets

from destdocs import models, serializers


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Project.objects.all().order_by('-created')
    serializer_class = serializers.ProjectSerializer
