from django.test import TestCase, Client
from django.urls import reverse
from score.models import Song, Playlist, Artist

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.song_url = reverse('song')
        self.playlist_url = reverse('playlist')
        self.artist1 = Artist.objects.create(
            name='Elsa mayori'
        )
         
        self.playlist1 = Playlist.objects.create(
            title='satu pop',
            created='2023-12-12'
        ) 

    def test_song_GET(self):
        client = Client()

        response = client.get(reverse('song'))

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'song.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_playlist_POST_add_new_playlist(self):
        response = self.client.post(self.playlist_url, {
            'title' : 'cobacoba',
            'created' : '2022-01-01',
            'save' : 'save'
        }
        ) 
 

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Playlist.objects.count(), 2)

    def test_song_POST_add_song_to_playlist(self):
        song2 = Song.objects.create(
            title='Newyork',
            releasedDate='2022-01-01',
            artist=self.artist1
        )

        response = self.client.post(self.song_url, {
            'songId': song2.id,
            'playlistId': self.playlist1.id,
            'add':song2.id
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.playlist1.songs.first().title, 'Newyork')
    
    def test_playlist_POST_delete_playlist(self):
        response = self.client.post(self.playlist_url, {
            'delete': self.playlist1.id
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Playlist.objects.count(), 0)