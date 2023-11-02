"""
URL configuration for music_catalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from catalogapp.web.views import AlbamMgt, CreateYourPlaylist, TrackObj, albumDetails, createAlbam, deleteTracks, home, PlayListMgt, removeFromPlayList, updatePlaylist, uploadTracks


urlpatterns = [
    path('', home,name='home'),
    path('upload_tracks', uploadTracks,name='upload_tracks'),
    # path('upload_tracks_add', uploadTracksAlbum,name='upload_tracks_add'),
    path('create_your_playlist', CreateYourPlaylist,name='create_your_playlist'),
    path('create_albam', createAlbam,name='create_albam'),
    path('delete_tracks/<str:uuid>/', deleteTracks,name='delete_tracks'),
    path('update_playlist/<str:uuid>', updatePlaylist,name='update_playlist'),
    path('tracks_mgt/delete_playlist_tracks/<str:uuid>/<str:track_uuid>/', removeFromPlayList,name='delete_playlist_tracks'),
    path('albam_mgt/tracks_mgt/<str:album>', albumDetails,name='album_mgt_details'),
    # path('read_playlist/<str:uuid>/', readPlaylist,name='read_playlist'),
    path('play_list', PlayListMgt.as_view(),name='play_list'),
    path('tracks_mgt/', TrackObj.as_view(),name='tracks_mgt'),
    path('albam_mgt/', AlbamMgt.as_view(),name='albam_mgt'),
]
