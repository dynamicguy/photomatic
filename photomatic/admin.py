__author__ = 'ferdous'

from django.contrib import admin
from photomatic.models import *

#class AlbumAdmin(admin.ModelAdmin):
#    list_display = ('title', 'description')
#    list_per_page = 100
#    ordering = ['title', ]
#    search_fields = ['title', 'description', ]
#    list_filter = ['photo']
#
#
#class PhotoAdmin(admin.ModelAdmin):
#    list_display = ('title', 'description', 'file')
#    list_per_page = 100
#    ordering = ['title', ]
#    search_fields = ['title', 'description', ]
#    list_filter = ['album']

#admin.site.register(Album, AlbumAdmin)
#admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Message)