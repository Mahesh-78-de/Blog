from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'


status_choices = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts')
    author =models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    short_description = models.TextField(max_length=300 , blank=True)
    blog_body = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Comments(models.Model):
    user =models.ForeignKey(User , on_delete=models.CASCADE)
    blog =models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
