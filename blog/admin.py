from django.contrib import admin
from .models import BlogPost, Category, Comments


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_featured',)
    list_filter = ('status', 'category', 'is_featured')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)

admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comments)

# Register your models here.
