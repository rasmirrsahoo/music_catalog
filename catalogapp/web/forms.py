from django import forms

from catalogapp.models import Album, PlayList, Track

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'album', 'artist', 'music_file']



class PlayListForm(forms.ModelForm):
    class Meta:
        model = PlayList
        fields = ['title', 'track']
        

class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist']
