from django.shortcuts import render

from blog.models import BlogPost, Category

def home(request):
    categories = Category.objects.all()
    featured_posts = BlogPost.objects.filter(is_featured=True, status='Published').order_by('-created_at')
    posts = BlogPost.objects.filter(is_featured=False, status='Published').order_by('-created_at')
    context = {
        'categories': categories,
        'featured_posts': featured_posts ,
        'posts': posts ,
    }

    return render(request, 'home.html', context)