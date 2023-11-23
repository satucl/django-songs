from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.song, name='song'),
    path('song', views.song, name='song'),
    path('playlist', views.playlist, name='playlist'),
    path('playlist/<int:playlistId>', views.playlistItem, name='playlistItem')

]
