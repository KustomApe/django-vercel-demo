from django.contrib import admin
from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('name', 'price')


admin.site.register(Vehicle, VehicleAdmin)
