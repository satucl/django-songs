from django.shortcuts import render
from django.contrib import messages
from score.models import Song, Playlist, PlaylistItem
from score.forms import PlaylistForm


def song(request):
    context = {}
    songs = Song.objects.all()
    playlists = Playlist.objects.all()
    context['songs'] = songs
    context['playlists'] = playlists
    context['title'] = 'Song List'

    if request.method == 'POST':
        if 'add' in request.POST:
            songId = request.POST.get('add')
            playlistId = request.POST.get('playlistId')
            added_playlist = Playlist.objects.get(id=playlistId)
            added_song = Song.objects.get(id=songId)
            added_playlist.songs.add(added_song)
            messages.success(request, "success adding song")
            
    return render(request, 'song.html', context)

def playlistItem(request, playlistId):
    context = {}
    playlist = Playlist.objects.get(id=playlistId) 
    context['playlist'] = playlist
    context['title'] = 'Playlist Items'

    if request.method == 'POST':
        if 'delete' in request.POST:
            songId = request.POST.get('delete')
            song = Song.objects.get(id=songId)
            playlist.songs.remove(song)
            playlist.save()

    return render(request, 'playlistItem.html', context)

def playlist(request):
    context = {}
    form = PlaylistForm()   
    playlists = Playlist.objects.all()
    context['playlists'] = playlists
    context['title'] = 'PlayList'

    if request.method == 'POST':
        if 'save' in request.POST:
            form = PlaylistForm(request.POST)
            form.save()
            form = PlaylistForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            playlist = Playlist.objects.get(id=pk)
            playlist.delete() 

    return render(request, 'playlist.html', context)

def about(request):
    context = {} 
    context['title'] = 'About'
    return render(request, 'about.html', context)
