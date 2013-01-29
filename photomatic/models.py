__author__ = 'ferdous'

from django.db import models
from django.contrib.auth.models import User
import datetime

class Album(models.Model):
    user = models.ForeignKey(User, default=2)
    fb_album_id = models.CharField('fb_album_id', max_length=200, null=True, blank=True)
    title = models.CharField('title', max_length=200)
    description = models.CharField('description', max_length=200, null=True, blank=True)
    created = models.DateTimeField('date created', default=datetime.datetime.now)
    updated = models.DateTimeField('last updated', auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'albums'


class Photo(models.Model):
    album = models.ForeignKey('Album', null=True, blank=True)
    title = models.CharField('title', max_length=200)
    description = models.CharField('description', max_length=200, null=True, blank=True)
    file = models.ImageField('file', upload_to='photos/%Y/%m/%d')
    created = models.DateTimeField('date created', default=datetime.datetime.now)
    updated = models.DateTimeField('last updated', auto_now_add=True)

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'photos'


class Message(models.Model):
    user = models.ForeignKey(User, default=2)
    next_page = models.CharField('next_page', max_length=255)
    status = models.CharField('status', max_length=40, default='awaiting')
    created = models.DateTimeField('date created', default=datetime.datetime.now)
    updated = models.DateTimeField('last updated', auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.next_page

