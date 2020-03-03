from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.


class AuthFieldsMixin:
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='created_by_set')
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                  on_delete=models.SET_NULL, related_name='updated_by_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class AccessFieldsMixin:
    access_mode = models.CharField(max_length=50, choices=(('PUBLIC', 'Public'), (
        'PRIVATE', 'Private'), ('INVITATION', 'Invited Only'), ('FRIENDS', 'Friends Only'),))
    is_published = models.BooleanField(default=False)


class Comment(AuthFieldsMixin, models.Model):
    '''Comments can be added to any object in the system'''
    comment = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment


class Recommendation(AuthFieldsMixin, models.Model):
    '''Recommendations can be added to any object in the system'''
    comment = models.TextField()
    recipients = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment
