# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import Projects,SiteInfo,ProjectQuery,Query
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name']

class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ['site_name']

class QueryAdmin(admin.ModelAdmin):
    list_display = ['title']

class ProjectQueryAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    # def has_add_permission(self, request):
    #     return False
    
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(SiteInfo,SiteInfoAdmin)
admin.site.register(Query,QueryAdmin)
admin.site.register(ProjectQuery,ProjectQueryAdmin)