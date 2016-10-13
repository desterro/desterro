# coding: utf-8

from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.name


class Version(BaseModel):
    project = models.ForeignKey(Project, related_name='versions')
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number

    class Meta:
        index_together = ['project', 'number']
