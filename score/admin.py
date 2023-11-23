from django.contrib import admin
from score.models import Song
from score.models import Artist
from score.models import Playlist
from score.models import PlaylistItem

class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist']

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name'];

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']

class PlaylistItemAdmin(admin.ModelAdmin):
    list_display = ['playlist']
 
admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(PlaylistItem, PlaylistItemAdmin)