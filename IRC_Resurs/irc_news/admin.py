from .models import *
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_display=('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug":("title",)}


class CategorieAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}



admin.site.register(News, NewsAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Pictures)
admin.site.register(Comentari)
admin.site.register(ProIrc)
admin.site.register(Users)








