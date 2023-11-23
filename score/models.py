from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=50)
    releasedDate = models.DateField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title

class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.playlist.title