from django.contrib import admin

from .models import Plan, Project, Timeline, Video

# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    autocomplete_fields = ('timeline',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    search_fields = ('project',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass