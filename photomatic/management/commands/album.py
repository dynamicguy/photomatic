from pprint import pprint

__author__ = 'ferdous'

from photomatic.management.commands import facebook
from django.core.management.base import BaseCommand, CommandError
from photomatic.models import *
from photomatic.facebook import get_access_token
from urllib2 import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib2 import urlparse

class Command(BaseCommand):
    args = '<album_id album_id ...>'
    help = 'fetch photos for given album'
    color_style = 'dark'

    def get_photos(self, album):
        u = album.user
        token = get_access_token(u)
        graph = facebook.GraphAPI(token)
        photos = graph.get_object(album.fb_album_id + "/photos", fields='id,source', limit=2)
        next_page = photos.get('paging').get('next')
        for photo in photos.get('data'):
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(photo.get('source')).read())
            img_temp.flush()
            photo_object = Photo.objects.create(title=photo.get('id'),
                description=photo.get('created_time'),
                album=album,
                file=File(img_temp))
            pprint(photo_object.filename)
            self.stdout.write('Successfully fetched photo for source "%s"\n' % photo.get('source'))
        msg = Message.objects.create(next_page=next_page, user=u, status='awaiting')
        self.stdout.write('New message queued with this page "%s"\n' % msg.next_page)


    def fetch_photos_from_msg(self, album, msg=None):
        u = album.user
        token = get_access_token(u)
        graph = facebook.GraphAPI(token)

        if msg.status == 'awaiting':
            parts = urlparse.urlparse(msg.next_page)
            qs = urlparse.parse_qs(parts.query)
            after = qs.get('after')[0]
            photos = graph.get_object(album.fb_album_id + "/photos", fields='id,source', limit=2, after=after)
            new_next_page = photos.get('paging').get('next')
            new_msg = Message.objects.create(next_page=new_next_page, user=u, status='awaiting')
            for photo in photos.get('data'):
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(photo.get('source')).read())
                img_temp.flush()
                photo_object = Photo.objects.create(title=photo.get('id'),
                    description=photo.get('created_time'),
                    album=album,
                    file=File(img_temp))
                pprint(photo_object.filename)
                self.stdout.write('Successfully fetched photo for source "%s"\n' % photo.get('source'))
            msg.status = 'done'
            msg.save()
            self.stdout.write('Finished this queue "%s"\n' % new_msg.next_page)

    def handle(self, *args, **options):
        if not args:
            raise CommandError('you need to provide an album id as parameter. example:\n ./manage.py album 1\n')

        for album_id in args:
            try:
                album = Album.objects.get(pk=int(album_id))
                my_undone_msgs = Message.objects.filter(status='awaiting', user=album.user)
                if len(my_undone_msgs) > 0:
                    self.fetch_photos_from_msg(album, my_undone_msgs[0])
                else:
                    self.get_photos(album)




            except Album.DoesNotExist:
                raise CommandError('Album "%s" does not exist' % album_id)