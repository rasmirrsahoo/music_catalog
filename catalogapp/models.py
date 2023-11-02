from django.db import models
import uuid
# Create your models here.

class Artist(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4) # unique=True, 
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Album(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4) # unique=True, 
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null = True)
    def __str__(self):
        return self.title
    
class Track(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4) # unique=True, 
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    music_file = models.FileField(upload_to='music_tracks/')
    def __str__(self):
        return self.title

class PlayList(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4) # unique=True, 
    title = models.CharField(max_length=255)
    track = models.ManyToManyField(Track)