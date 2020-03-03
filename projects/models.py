from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from common.models import (AccessFieldsMixin, AuthFieldsMixin, Comment,
                           Recommendation)

# Create your models here.


class Project(AuthFieldsMixin, models.Model):
    '''A person can have several projects'''
    name = models.CharField(max_length=500)


class Timeline(AuthFieldsMixin, AccessFieldsMixin, models.Model):
    '''Each project can have only one Timeline
    TODO: The timeline can be implemented with a calendar in mind.
    '''
    project = models.OneToOneField(Project, on_delete=models.CASCADE)


class Plan(AuthFieldsMixin, AccessFieldsMixin, models.Model):
    '''One or more plans can be added to a timeline'''
    title = models.CharField(max_length=500)
    cover_time = models.DateTimeField()
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    content = models.TextField()
    comments = GenericRelation(Comment, related_query_name='plan_comments')
    recommendations = GenericRelation(
        Recommendation, related_query_name='plan_recommendations')


class Video(AuthFieldsMixin, AccessFieldsMixin, models.Model):
    '''Videos can be added to a timeline covering specified time'''
    title = models.CharField(max_length=500)
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    cover_time = models.DateTimeField()
    video_file = models.FileField(max_length=500, upload_to='videos')
    comments = GenericRelation(Comment, related_query_name='video_comments')
    recommendations = GenericRelation(
        Recommendation, related_query_name='video_recommendations')
