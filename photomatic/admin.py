__author__ = 'ferdous'

from django.contrib import admin
from photomatic.models import Album, Photo

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_per_page = 100
    ordering = ['title', ]
    search_fields = ['title', 'description', ]
    list_filter = ['photo']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_per_page = 100
    ordering = ['title', ]
    search_fields = ['title', 'description', ]
    list_filter = ['album']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)