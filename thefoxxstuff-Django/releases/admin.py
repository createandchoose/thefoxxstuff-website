from django.contrib import admin


from .models import Album

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'data_created', 'draft')
    list_display_links = ('id', 'title')

admin.site.register(Album, NewsAdmin)
