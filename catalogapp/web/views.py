from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from catalogapp.models import Album, PlayList, Track
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from catalogapp.web.forms import AlbumCreateForm, PlayListForm, TrackForm

# Create your tests here.
def home(request, **kwargs):
    return render(request,'home.html')

class PlayListMgt(ListView):
    
    model = PlayList 
    template_name = 'playlist.html'
    context_object_name = 'playlists'
    
    
    def get_context_data(self, **kwargs):
        param = self.request.GET.get('param_uuid', None)
        context = super().get_context_data(**kwargs)
        context['form'] = PlayListForm()
        # context['param'] = param
        return context
    def get_queryset(self): 
        data = PlayList.objects.all()
        return data
    
    
class TrackObj(ListView):
    
    model = Track 
    template_name = 'tracks.html'
    context_object_name = 'tracks'
    
    def get_context_data(self, **kwargs):
        param = self.request.GET.get('param_uuid', None)
        context = super().get_context_data(**kwargs)
        context['form'] = TrackForm()
        context['param'] = param
        return context
    
    
    def get_queryset(self): 
        param = self.request.GET.get('param_uuid', None)
        if param is not None:
            objs = PlayList.objects.get(uuid = param)
            print(objs.track.values_list('uuid', flat=True),"=====>")
            data = Track.objects.filter(uuid__in = objs.track.values_list('uuid', flat=True))
            
        else:
            data = Track.objects.all()
        return data



# class TrackMgt(View):
def uploadTracks(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or track listing
    else:
        form = TrackForm()
    
    return redirect('home')

# class TrackMgt(View):
# def uploadTracksAlbum(request):
#     title = request.POST.get('title')
#     album_id = request.POST.get('album_id')
#     file = request.FILES.getlist('file')
#     print(album_id,"==============")
#     if request.method == 'POST':
#         albam_obj = Album.objects.get(id=album_id)
#         for music in album_id:
#             track = Track()
#             track.title = title
#             track.album = albam_obj
            
#         return redirect('home')  # Redirect to a success page or track listing
#     else:
#         form = TrackForm()
    
#     return redirect('home')


def deleteTracks(request, uuid):
    print(uuid)
    Track.objects.filter(uuid=uuid).delete()
    return redirect('tracks_mgt')


def updatePlaylist(request, uuid):
    # uuid = request.POST.get('uuid')
    # track = request.POST.getlist('track')

    if request.method == 'POST':
        # track_obj = Track.objects.filter(uuid__in = track)
        objs = PlayList.objects.filter(uuid=uuid).last()
        
        form_data = PlayListForm(request.POST, instance=objs)
        if form_data.is_valid():
            print(form_data,"============")
            
    #     if objs is not None:
    #         # for i in track_obj:
    #         objs.track.set(track_obj)
    #         objs.save()
    #         #     print(track_obj,"============")
    #         #     objs.track.add(i.uuid)
    #             # objs.save()
    # else:
    #     form = PlayListForm(instance=uuid)

    # return render(request, 'update_playlist.html', {'form': form})
    return redirect('play_list')



def removeFromPlayList(request, uuid,track_uuid):
    print(uuid,"======",track_uuid)
    objs = PlayList.objects.get(uuid = uuid)
    track = Track.objects.get(uuid=track_uuid)
    objs.track.remove(track)
    # Track.objects.filter(uuid=uuid).delete()
    return redirect('tracks_mgt')


def albumDetails(request, album):
    # print(album,"======",album)
    objs = Track.objects.filter(album__uuid = album)
    
    print(objs)
    album_name = objs.last().album
    return render(request, 'album_track.html', {'tracks': objs, 'album':album_name})



def CreateYourPlaylist(request):
    if request.method == 'POST':
        form = PlayListForm(request.POST, request.FILES)
        print(form.is_valid(),"===============")
        if form.is_valid():
            form.save()
            
            return redirect('home')  # Redirect to a success page or track listing
        else:
            print(form.errors)
            form = PlayListForm()
    
    return redirect('home')



class AlbamMgt(ListView):
    
    model = Album 
    template_name = 'albams.html'
    context_object_name = 'albams'
    
    def get_context_data(self, **kwargs):
        param = self.request.GET.get('param_uuid', None)
        context = super().get_context_data(**kwargs)
        context['form'] = AlbumCreateForm()
        context['param'] = param
        return context
    
    
    def get_queryset(self): 
        param = self.request.GET.get('param_uuid', None)
        objs = Album.objects.all()
        
        return objs


def createAlbam(request):
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST, request.FILES)
        print(form.is_valid(),"===============")
        if form.is_valid():
            form.save()
            print('=====')
            return redirect('albam_mgt')  # Redirect to a success page or track listing
        else:
            print(form.errors)
            form = AlbumCreateForm()
    
    return redirect('home')