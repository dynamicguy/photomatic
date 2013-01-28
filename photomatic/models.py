__author__ = 'ferdous'

from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    user = models.ForeignKey(User, default=2)
    title = models.CharField('title', max_length=200)
    description = models.CharField('description', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'albums'


class Photo(models.Model):
    album = models.ForeignKey('Album', null=True, blank=True)
    title = models.CharField('title', max_length=200)
    description = models.CharField('description', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'photos'
