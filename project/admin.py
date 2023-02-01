from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'description')

admin.site.register(Item, ItemAdmin)