
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from blog.models import BlogPost, Category
from blog_main.forms import RegistrationForm
from pages.models import About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import auth

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

# logic to register a new user to the website.

def register(request):

    form= RegistrationForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = "Registration successful! You can now log in."
        else:
            context['error'] = "Please correct the errors below."

    return render(request, 'register.html', context)


# logic to log in an existing user to the website.
def login(request):
    form =AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
            
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

# logic to log out a logged in user from the website.
def logout(request):
    auth.logout(request)
    return redirect('home')