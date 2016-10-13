# coding: utf-8

from django.contrib import admin

from destdocs import models


class VersionAdmin(admin.TabularInline):
    model = models.Version
    fields = ['number', 'created', 'modified']
    readonly_fields = ['created', 'modified']
    extra = 0


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [VersionAdmin]
