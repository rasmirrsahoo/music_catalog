from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.status import *
from catalogapp.apis.serializers import AlbumCreateSerializer, AlbumManagementSerializer, AlbumUpdateSerializer, ArtistCreateSerializer, ArtistManagementSerializer, ArtistUpdateSerializer, PlayListCreateSerializer, PlayListManagementSerializer, PlayListUpdateSerializer, TrackCreateSerializer, TrackManagementSerializer, TrackUpdateSerializer
from catalogapp.models import Album, Artist, PlayList, Track
from rest_framework.response import Response
from rest_framework import parsers

# Create your views here.

class ArtistManagement(viewsets.ModelViewSet):
    serializer_class = ArtistManagementSerializer
    http_method_names = ['get','post','put','delete']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ArtistCreateSerializer
        if self.action == 'retrieve':
            return self.serializer_class
        elif self.action == "update":
            return  ArtistUpdateSerializer
        else:
            return self.serializer_class
    
    def get_queryset(self):
        data=Artist.objects.all().order_by('-uuid')
        return data
    
    def list(self, request, *args, **kwargs):
        data=Artist.objects.all().order_by('-uuid')
        serializer = ArtistManagementSerializer(data,many=True)
        context=({'message':"data found successfully","data":serializer.data})
        return Response(context,status=HTTP_200_OK)
    
    def create(self,request):
        try:
            
            serializer = ArtistCreateSerializer(data=request.data)
            if serializer.is_valid():
                # serializer.save()
            
                data = serializer.data
            
                context={"status":True,"message":"Created Successfully"}
                return Response(context, status=HTTP_201_CREATED)
            else:
              
                context={"status":False,"message":"Artist not created",'error' : serializer.errors}
                
                return Response(context, status=HTTP_400_BAD_REQUEST) 
            
        except Exception as e:
            context = {'status': False, 'message': {"error": str(e)}}
            return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)

            
           
    def destroy(self, request,pk):
        try:
            data = Artist.objects.filter(uuid=pk).last()
            if data:
                data.delete()
                context={'status':True,'message':"Artist deleted successfully"}
                return Response(context,status=HTTP_200_OK)
            else:
                
                context={'status':True,'message':"No Record found"}
                return Response(context,status=HTTP_404_NOT_FOUND)
            
        except Exception as e:
            context = {'status': False, 'message': {"error": str(e)}}
            return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self,request,pk):
        try:
            
            user_obj=Artist.objects.filter(uuid=pk).last()
          
            serialized_data = ArtistUpdateSerializer(data=request.data,context={'request':request,"user_obj":user_obj})
            if serialized_data.is_valid():
                    context={'status':True,'message':"Artist updated successfully"}
                    return Response(context,status=HTTP_200_OK)
                
            else:
                    context={'status':False,'message':serialized_data.errors}
                    return Response(context,status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            context={'status':False,'message':"Something went wrong"}
            return Response(context,status=HTTP_500_INTERNAL_SERVER_ERROR)
        

class AlbumManagement(viewsets.ModelViewSet):
    serializer_class = AlbumManagementSerializer
    http_method_names = ['get','post','put','delete']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return AlbumCreateSerializer
        if self.action == 'retrieve':
            return self.serializer_class
        elif self.action == "update":
            return  AlbumUpdateSerializer
        else:
            return self.serializer_class
    
    def get_queryset(self):
        data=Artist.objects.all().order_by('-uuid')
        return data
    
    def list(self, request, *args, **kwargs):
        data=Album.objects.all().order_by('-uuid')
        serializer = AlbumManagementSerializer(data,many=True)
        context=({'message':"data found successfully","data":serializer.data})
        return Response(context,status=HTTP_200_OK)
    
    def create(self,request):
        try:
            
            serializer = AlbumCreateSerializer(data=request.data)
            if serializer.is_valid():            
                data = serializer.data
            
                context={"status":True,"message":"Created Successfully"}
                return Response(context, status=HTTP_201_CREATED)
            else:
              
                context={"status":False,"message":"Album not created",'error' : serializer.errors}
                
                return Response(context, status=HTTP_400_BAD_REQUEST) 
            
        except Exception as e:
            context = {'status': False, 'message': {"error": str(e)}}
            return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)

            
           
    def destroy(self, request,pk):
        try:
            data = Album.objects.filter(uuid=pk).last()
            if data:
                data.delete()
                context={'status':True,'message':"Album deleted successfully"}
                return Response(context,status=HTTP_200_OK)
            else:
                
                context={'status':True,'message':"No Record found"}
                return Response(context,status=HTTP_404_NOT_FOUND)
            
        except Exception as e:
            context = {'status': False, 'message': {"error": str(e)}}
            return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self,request,pk):
        # try:
            
            user_obj=Album.objects.filter(uuid=pk).last()
          
            serialized_data = AlbumUpdateSerializer(data=request.data,context={'request':request,"user_obj":user_obj})
            if serialized_data.is_valid():
                context={'status':True,'message':"Album updated successfully"}
                return Response(context,status=HTTP_200_OK)
                
            else:
                    context={'status':False,'message':serialized_data.errors}
                    return Response(context,status=HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     context={'status':False,'message':"Something went wrong"}
        #     return Response(context,status=HTTP_500_INTERNAL_SERVER_ERROR)
        

class TrackManagement(viewsets.ModelViewSet):
    serializer_class = TrackManagementSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    http_method_names = ['get','post','put','delete']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TrackCreateSerializer
        if self.action == 'retrieve':
            return self.serializer_class
        elif self.action == "update":
            return  TrackUpdateSerializer
        else:
            return self.serializer_class
    
    def get_queryset(self):
        data=Track.objects.all().order_by('-uuid')
        return data
    
    def list(self, request, *args, **kwargs):
        data=Track.objects.all().order_by('-uuid')
        serializer = TrackManagementSerializer(data,many=True)
        context=({'message':"data found successfully","data":serializer.data})
        return Response(context,status=HTTP_200_OK)
    
    def create(self,request):
        try:
            
            serializer = TrackCreateSerializer(data=request.data)
            if serializer.is_valid():
                # serializer.save()
            
                data = serializer.data
            
                context={"status":True,"message":"Created Successfully"}
                return Response(context, status=HTTP_201_CREATED)
            else:
              
                context={"status":False,"message":"Track not created",'error' : serializer.errors}
                
                return Response(context, status=HTTP_400_BAD_REQUEST) 
            
        except Exception as e:
            context = {'status': False, 'message': {"error": str(e)}}
            return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)

            
           
    def destroy(self, request,pk):
        try:
            data = Track.objects.filter(uuid=pk).last()
            if data:
                data.delete()
                context={'status':True,'message':"Track deleted successfully"}
                return Response(context,status=HTTP_200_OK)
            else:
                
                context={'status':True,'message':"No Record found"}
                return Response(context,status=HTTP_404_NOT_FOUND)
            
        except Exception as e:
            context = {'status': False, 'message': {"error": str(e)}}
            return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self,request,pk):
        try:
            
            user_obj=Track.objects.filter(uuid=pk).last()
          
            serialized_data = TrackUpdateSerializer(data=request.data,context={'request':request,"user_obj":user_obj})
            if serialized_data.is_valid():
                    context={'status':True,'message':"Track updated successfully"}
                    return Response(context,status=HTTP_200_OK)
                
            else:
                    context={'status':False,'message':serialized_data.errors}
                    return Response(context,status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            context={'status':False,'message':"Something went wrong"}
            return Response(context,status=HTTP_500_INTERNAL_SERVER_ERROR)
        
        
#@!!!!!!!!!!!!!!@@@@@@@





class PlayListManagement(viewsets.ModelViewSet):
    serializer_class = PlayListManagementSerializer
    # parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    http_method_names = ['get','post','put','delete']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PlayListCreateSerializer
        if self.action == 'retrieve':
            return self.serializer_class
        elif self.action == "update":
            return  PlayListUpdateSerializer
        else:
            return self.serializer_class
    
    def get_queryset(self):
        data=PlayList.objects.all().order_by('-uuid')
        return data
    
    def list(self, request, *args, **kwargs):
        data=PlayList.objects.all().order_by('-uuid')
        serializer = PlayListManagementSerializer(data,many=True)
        context=({'message':"data found successfully","data":serializer.data})
        return Response(context,status=HTTP_200_OK)
    
    def create(self,request):
        # try:
            
            serializer = PlayListCreateSerializer(data=request.data)
            if serializer.is_valid():
                # serializer.save()
            
                data = serializer.data
            
                context={"status":True,"message":"Created Successfully"}
                return Response(context, status=HTTP_201_CREATED)
            else:
              
                context={"status":False,"message":"Playlist not created",'error' : serializer.errors}
                
                return Response(context, status=HTTP_400_BAD_REQUEST) 
            
        # except Exception as e:
        #     context = {'status': False, 'message': {"error": str(e)}}
        #     return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)

            
           
    def destroy(self, request,pk):
        try:
            data = PlayList.objects.filter(uuid=pk).last()
            if data:
                data.delete()
                context={'status':True,'message':"Playlist deleted successfully"}
                return Response(context,status=HTTP_200_OK)
            else:
                
                context={'status':True,'message':"No Record found"}
                return Response(context,status=HTTP_404_NOT_FOUND)
            
        except Exception as e:
            context = {'status': False, 'message': {"error": str(e)}}
            return Response(context, status=HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self,request,pk):
        try:
            
            user_obj=PlayList.objects.filter(uuid=pk).last()
          
            serialized_data = PlayListUpdateSerializer(data=request.data,context={'request':request,"user_obj":user_obj})
            if serialized_data.is_valid():
                    context={'status':True,'message':"Playlist updated successfully"}
                    return Response(context,status=HTTP_200_OK)
                
            else:
                    context={'status':False,'message':serialized_data.errors}
                    return Response(context,status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            context={'status':False,'message':"Something went wrong"}
            return Response(context,status=HTTP_500_INTERNAL_SERVER_ERROR)
        