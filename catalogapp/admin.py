from django.contrib import admin
from catalogapp.models import *
# Register your models here.

# admin.site.register(Track)
# admin.site.register(Album)
# admin.site.register(Artist)
# admin.site.register(PlayList)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name')
    search_fields = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'artist')
    list_filter = ('artist',)
    search_fields = ('title', 'artist__name')
    raw_id_fields = ('artist',)

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'artist', 'album')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__name', 'album__title')
    raw_id_fields = ('artist', 'album')

@admin.register(PlayList)
class PlayListAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title')
    filter_horizontal = ('track',)  # Use filter_horizontal for many-to-many fields.

    # Add CRUD functionality directly within the admin panel
    actions = ['duplicate_selected']

    def duplicate_selected(self, request, queryset):
        for playlist in queryset:
            playlist.pk = None  # Create a copy of the selected playlist
            playlist.save()
        self.message_user(request, f"Selected playlists duplicated successfully.")

    duplicate_selected.short_description = "Duplicate selected playlists"

    actions = ['delete_selected']

    # delete_selected.short_description = "Delete selected playlists"
