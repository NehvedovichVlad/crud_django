from django.contrib import admin

from accounts.models import Person
from django.utils.safestring import mark_safe

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'created_info', 'update_info',  'get_photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'age')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    fields = ('name', 'age', 'email',  'photo', 'created_info', 'update_info')
    readonly_fields = ('get_photo', 'created_info', 'update_info',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="65">')
        else:
            return 'Фото не установленно'

    get_photo.short_description = 'Фото'