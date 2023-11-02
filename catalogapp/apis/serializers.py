from rest_framework import  serializers

from catalogapp.models import Album, Artist, PlayList, Track


class ArtistManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["uuid","name"]
   
class ArtistUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["name"]

    def validate(self,attrs):
        user_obj = self.context.get('user_obj')
        
        user_check = Artist.objects.filter(uuid=user_obj.uuid).last()
        if user_check:
           
            obj = user_check        
            obj.name=attrs["name"] if attrs.get("name") else user_obj.name
           
            obj.save()
        return attrs
        


class ArtistCreateSerializer(serializers.ModelSerializer):
    name= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid name.'})
    
    class Meta:
        model = Artist
        fields = ["name"]
    
    
    def validate_name(self, attrs):
        print(attrs,'s')
        # print(str(attrs.get("name")),'ccvv')
        if not attrs:
            raise serializers.ValidationError('Name cannot be blank')
        return attrs
    
    def validate(self,attrs):
        name = str(attrs.get("name"))
            
        return attrs
    

#???????


class AlbumManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["uuid","artist","title"]
   
class AlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["title","artist"]

    def validate(self,attrs):
        user_obj = self.context.get('user_obj')
        
        user_check = Album.objects.filter(uuid=user_obj.uuid).update(
            title=attrs.get("title") if attrs.get("title") else user_obj.title,
            artist=attrs.get("artist") if attrs.get("artist") else user_obj.artist
            
        )
        # .last()
        # if user_check:
           
        #     obj = user_check   
        #     print(obj,user_check,'rrrtrrt',user_obj)     
            
           
        #     obj.save()
        return attrs
        


class AlbumCreateSerializer(serializers.ModelSerializer):
    title= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid title.'})
    artist= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid artist.'})
    
    
    class Meta:
        model = Album
        fields = ["title",'artist']
    
    
    def validate_name(self, attrs):
        print(attrs,'s')
        # print(str(attrs.get("name")),'ccvv')
        if not attrs['title']:
            raise serializers.ValidationError('title cannot be blank')
        
        if not attrs['artist']:
            raise serializers.ValidationError('artist cannot be blank')
        return attrs
    
    def validate(self,attrs):
        title = str(attrs.get("title"))
        artist = str(attrs.get("artist"))
        obj = Album()
        obj.title = title
        artist_obj = Artist.objects.get(uuid = artist)
        print(artist_obj ,'xxxx')
        obj.artist = artist_obj
        obj.save()

            
        return attrs
    
#@!!!!!!!!!!!!

class TrackManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["uuid","artist","title",'album','music_file']
   
class TrackUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["title","artist",'album','music_file']

    def validate(self,attrs):
        user_obj = self.context.get('user_obj')
        
        user_check = Track.objects.filter(uuid=user_obj.uuid).last()
        if user_check:
           
            obj = user_check        
            obj.name=attrs["title"] if attrs.get("title") else user_obj.title
           
            obj.save()
        return attrs
        
#@@@

class TrackCreateSerializer(serializers.ModelSerializer):
    title= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid title.'})
    artist= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid artist.'})
    album= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid album.'})
    music_file= serializers.FileField(required = True,error_messages={'invalid': 'Please enter a valid music file.'})
    
    
    class Meta:
        model = Track
        fields = ["title",'artist','album','music_file']
    
    
    def validate_name(self, attrs):
        print(attrs,'s')
        # print(str(attrs.get("name")),'ccvv')
        if not attrs['title']:
            raise serializers.ValidationError('title cannot be blank')
        
        if not attrs['artist']:
            raise serializers.ValidationError('artist cannot be blank')
        
        if not attrs['album']:
            raise serializers.ValidationError('album cannot be blank')
        
        if not attrs['music_file']:
            raise serializers.ValidationError('music file cannot be blank')
        return attrs
    
    def validate(self,attrs):
        title = str(attrs.get("title"))
        artist = str(attrs.get("artist"))
        album = str(attrs.get("artist"))
        music_file = str(attrs.get("artist"))

        obj = Track()
        obj.title = title
        obj.artist_uuid = artist
        obj.album_uuid = album
        obj.music_file = music_file

        obj.save()

            
        return attrs
    
#$$$$$$$$$$$$$$$$$$



class PlayListManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ["uuid","track","title"]
   
class PlayListUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ["title","track"]

    def validate(self,attrs):
        user_obj = self.context.get('user_obj')
        
        user_check = PlayList.objects.filter(uuid=user_obj.uuid).last()
        if user_check:
           
            obj = user_check        
            obj.title=attrs["title"] if attrs.get("title") else user_obj.title
            obj.track_uuid=attrs["track"] if attrs.get("track") else user_obj.track
            
           
            obj.save()
        return attrs
        
#@@@

class PlayListCreateSerializer(serializers.ModelSerializer):
    title= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid title.'})
    track= serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid track.'})
    
    
    class Meta:
        model = PlayList
        fields = ["title",'track']
    
    
    def validate_name(self, attrs):
        print(attrs,'s')
        # print(str(attrs.get("name")),'ccvv')
        if not attrs['title']:
            raise serializers.ValidationError('title cannot be blank')
        
        if not attrs['track']:
            raise serializers.ValidationError('track cannot be blank')
        
        
        return attrs
    
    def validate(self,attrs):
        title = str(attrs.get("title"))
        track = str(attrs.get("track"))
        
        obj = PlayList()
        obj.title = title
        obj.track_uuid = track
        
        obj.save()

            
        return attrs