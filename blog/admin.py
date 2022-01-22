

from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'status')
    list_filter = ('status',)
    prepopulated_field = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
