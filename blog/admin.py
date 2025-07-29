from django.contrib import admin
from .models import Post
from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
   


admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published')
    list_filter = ('published', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
    ordering = ('-published',)

admin.site.register(Post, PostAdmin)
