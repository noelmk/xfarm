from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from .models import Comment, Recommendation


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    autocomplete_fields = ('content_type',)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    autocomplete_fields = ('content_type', 'recipients',)
