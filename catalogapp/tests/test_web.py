from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from catalogapp.models import Album, PlayList, Track
from django.urls import reverse

from catalogapp.web.forms import AlbumCreateForm, PlayListForm, TrackForm


class FirstTestCase(TestCase):
    # def setUp(self):
    #     # return super().setUp()
    #     print("====================///============")
    
    def test_upload_track(self):
        file = SimpleUploadedFile("test_track.mp3", b"file_content")

        response = self.client.post('upload_tracks', {'title': 'Test Track', 'music_file': file})
        self.assertEqual(response.status_code, 302)

        track = Track.objects.filter(title='Test Track').first()
        self.assertIsNotNone(track)
        self.assertTrue(track.music_file.name.startswith('music_tracks/'))
        
    def test_create_playlist_success(self):
        
        file = SimpleUploadedFile("test_playlist.txt", b"file_content")

        data = {
            'title': 'Test Playlist',
            'track': [1, 2],  
        }
        
        form_data = {
            'title': 'Test Playlist',
            'track': data['track'],
            'playlist_file': file,
        }
        response = self.client.post(reverse('create-playlist'), form_data, format='multipart')
        self.assertEqual(response.status_code, 302)

        playlist = PlayList.objects.filter(title='Test Playlist').first()
        self.assertIsNotNone(playlist)

        self.assertTrue(playlist.playlist_file.name.startswith('music_playlists/'))
        
    def test_playlist_management_view(self):
        
        PlayList.objects.create(title='Test Playlist')

        response = self.client.get(reverse('playlist-management'))

        self.assertEqual(response.status_code, 200)

        self.assertTrue('playlists' in response.context)
        self.assertTrue('form' in response.context)

        playlists = response.context['playlists']
        self.assertEqual(len(playlists), 1)
        self.assertEqual(playlists[0].title, 'Test Playlist')

        form = response.context['form']
        self.assertIsInstance(form, PlayListForm)
    
    def test_track_object_view(self):
        
        playlist = PlayList.objects.create(title='Test Playlist')
        
        track1 = Track.objects.create(title='Track 1', album=None, artist=None, music_file=None)
        track2 = Track.objects.create(title='Track 2', album=None, artist=None, music_file=None)
        playlist.track.add(track1, track2)

        response = self.client.get(reverse('track-object') + '?param_uuid=' + str(playlist.uuid))

        self.assertEqual(response.status_code, 200)

        self.assertTrue('tracks' in response.context)
        
        self.assertTrue('form' in response.context)
        self.assertTrue('param' in response.context)

        tracks = response.context['tracks']
        self.assertEqual(list(tracks), [track1, track2])

        form = response.context['form']
        self.assertIsInstance(form, TrackForm)
        param = response.context['param']
        self.assertEqual(param, str(playlist.uuid))
        
        
    def test_albam_management_view(self):
        album1 = Album.objects.create(title='Album 1', artist=None)
        album2 = Album.objects.create(title='Album 2', artist=None)

        response = self.client.get(reverse('albam-management'))

        self.assertEqual(response.status_code, 200)

        self.assertTrue('albams' in response.context)

        self.assertTrue('form' in response.context)

        self.assertFalse('param' in response.context)

        albams = response.context['albams']
        self.assertEqual(list(albams), [album1, album2])

        form = response.context['form']
        self.assertIsInstance(form, AlbumCreateForm)

    def test_create_albam(self):
        response = self.client.post(reverse('create-albam'), {'title': 'New Album'})

        self.assertEqual(response.status_code, 302)

        album = Album.objects.filter(title='New Album').first()
        self.assertIsNotNone(album)