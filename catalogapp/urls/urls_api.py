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
from rest_framework.routers import DefaultRouter


from catalogapp.apis.views import AlbumManagement, ArtistManagement, PlayListManagement, TrackManagement



router = DefaultRouter()
router.register('artist_management', ArtistManagement, basename='artist_management')
router.register('album_management', AlbumManagement, basename='album_management')
router.register('track_management', TrackManagement, basename='track_management')
router.register('playlist_management', PlayListManagement, basename='playlist_management')




urlpatterns = [
    # path('/home/', home,name='home'),
]
urlpatterns = router.urls
