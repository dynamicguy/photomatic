"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from photomatic.models import *
from django.contrib.auth.models import User


class AlbumModelTest(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            username='admin',
            password='admin',
            email='admin@local.host',
        )

    def test_creating_a_new_album_and_saving_it_to_the_database(self):
        """start by creating a new Album object with its title set """
        album = Album.objects.create(
            title="What's up?",
            description="What's up dude?",
            user=self.user,
        )
        album.fb_album_id='some id',
        album.save()

        # now check we can find it in the database again
        all_albums_in_database = Album.objects.all()
        self.assertEquals(len(all_albums_in_database), 1)
        only_album_in_database = all_albums_in_database[0]
        self.assertEquals(only_album_in_database, album)

        # and check that it's saved its two attributes: question and pub_date
        self.assertEquals(only_album_in_database.title, "What's up?")
        self.assertEquals(only_album_in_database.created, album.created)


class PhotoModelTest(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=2,
            username='user',
            password='user',
            email='user@local.host',
        )
        self.album = Album.objects.create(
            title="What's up?",
            description="What's up dude?",
            user=self.user,
        )

    def test_creating_a_new_photo_and_saving_it_to_the_database(self):
        """start by creating a new Photo object with its title set """
        photo = Photo.objects.create(
            title="What's up?",
            description="What's up dude?",
            album = self.album
        )
        photo.save()

        # now check we can find it in the database again
        all_photos_in_database = Photo.objects.all()
        self.assertEquals(len(all_photos_in_database), 1)
        only_photo_in_database = all_photos_in_database[0]
        self.assertEquals(only_photo_in_database, photo)

        # and check that it's saved its two attributes: question and pub_date
        self.assertEquals(only_photo_in_database.title, "What's up?")
        self.assertEquals(only_photo_in_database.created, photo.created)

