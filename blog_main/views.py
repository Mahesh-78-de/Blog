
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from blog.models import BlogPost, Category
from pages.models import About

def home(request):
    categories = Category.objects.all()
    featured_posts = BlogPost.objects.filter(is_featured=True, status='Published').order_by('-created_at')
    posts = BlogPost.objects.filter(is_featured=False, status='Published').order_by('-created_at')
    
    try:
        about = About.objects.get()
    except About.DoesNotExist:
        about = None

    context = {
        'categories': categories,
        'featured_posts': featured_posts ,
        'posts': posts ,
        'about' :about,
    }


    return render(request, 'home.html', context)


# logic to search for blogs based on the keyword entered by the user in the search bar.

def search(request):
    keyword = request.GET.get('Keyword')
    blogs = BlogPost.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status='Published').order_by('-created_at')
    context = {
        'keyword': keyword,
        'blogs': blogs,
    }
    return render(request, 'search.html', context)