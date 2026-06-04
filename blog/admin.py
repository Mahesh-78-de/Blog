from django.contrib import admin
from .models import BlogPost, Category


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status')
    list_filter = ('status', 'category', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)

admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)

# Register your models here.
