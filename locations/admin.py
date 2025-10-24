from django.contrib import admin

from locations.models import Place, PlaceImage


class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image', 'position')


class PlaceImageInline(admin.StackedInline):
    model = PlaceImage
    max_num = 10
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', 'description_long', 'lng', 'lat')
    inlines = [PlaceImageInline, ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)
