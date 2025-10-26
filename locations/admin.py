from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from locations.models import Place, PlaceImage


class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image', 'position')


class PlaceImageInlineForm(forms.ModelForm):
    class Meta:
        model = PlaceImage
        fields = '__all__'
        widgets = {'position': forms.HiddenInput}


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    form = PlaceImageInlineForm
    fields = ('image', 'preview', 'position_display', 'position')
    max_num = 10
    extra = 0
    readonly_fields = ('preview','position_display')
    sortable_field_name = 'position'

    def position_display(self, obj):
        return getattr(obj, 'position', '')

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    preview.short_description = 'Превью'
    position_display.short_description = 'Позиция'


class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short', 'description_long', 'lng', 'lat')
    inlines = [PlaceImageInline, ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)
