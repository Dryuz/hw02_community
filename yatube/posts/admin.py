from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'pub_date',
        'text',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_editable = ('group',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Group)
admin.site.register(Post, PostAdmin)
