from django.shortcuts import render
from blog.models import Category
def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_social_links(request):
    from pages.models import Social_links
    social_links = Social_links.objects.all()
    return dict(social_links=social_links)

