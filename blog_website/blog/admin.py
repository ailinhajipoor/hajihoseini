from django.contrib import admin

from .models import Post


@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'status', 'date_modified', 'author'
    )
    ordering = ('status', 'title')

# admin.site.register(Post)
# admin.site.register(Post,PostAdmin) bejeye in khate 3 ro neveshtim
