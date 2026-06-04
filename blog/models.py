from django.db import models



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'


status_choices = (
    ("Published", 'Published'),
    ("Draft", 'Draft'),
)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts')
    author =models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    blog_body = models.TextField()
    status = models.CharField(max_length=20, default="Draft", choices=status_choices)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


# Create your models here.
