from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost,Category


# Logic to retrieve and display posts for the given category_id
def category_posts(request, category_id):
    # Retrieve the category based on the provided category_id and return 404 if not found
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return render(request, '404.html', status=404)

    posts = BlogPost.objects.filter(category_id=category_id, status='Published').order_by('-created_at')
    featured_posts = posts.filter(is_featured=True)
    
    context = {
        'category': category,
        'posts': posts,
        'featured_posts': featured_posts,
        
    }
    return render(request, 'category_posts.html', context)

def blog_post(request, slug):
    single_blog = get_object_or_404(BlogPost, slug=slug, status='Published')

    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blog.html', context)


