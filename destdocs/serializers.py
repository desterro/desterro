# coding: utf-8

from rest_framework import serializers

from destdocs import models


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        exclude = ['project']


class ProjectSerializer(serializers.ModelSerializer):
    versions = VersionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
