from django.contrib import admin
from .models import DataKlass, Indexs


class DataKlassAdmin(admin.ModelAdmin):
    list_display = ('id', 'log', 'fik', 'klass', 'vyhods', 'balls')
    list_display_links = ('log', 'fik', 'klass')
    search_fields = ('log', 'fik', 'klass')

admin.site.register(DataKlass, DataKlassAdmin)


class IndexsAdmin(admin.ModelAdmin):
    list_display = ('id', 'log', 'ips', 'ipskol', 'curdate')
    list_display_links = ('id', 'log', 'ips', 'ipskol')
    search_fields = ('log', 'ips')

admin.site.register(Indexs, IndexsAdmin)


