from django.shortcuts import redirect, render ,get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Category ,BlogPost
from dashboard.form import CategoryForm, EditForm, PostForm ,UserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.

@login_required (login_url ='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = BlogPost.objects.all().count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

# creation of your view for categories 

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'dashboard/categories.html', context)

# adding the new category 

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()


    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

# Edit the category

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

# for deleting any categories

def delete_category(request,pk):
        category =get_object_or_404(Category ,pk=pk)
        category.delete()
        return redirect('categories')

# views for posts

def posts(request):
    posts = BlogPost.objects.all()
    context ={
        'posts':posts
    }
    return render(request, 'dashboard/posts.html',context)

def add_posts(request):
    if request.method =='POST':
        form=PostForm(request.POST  ,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)  # For saving data temporarily
            post.author =request.user
            title =form.cleaned_data['title']
            post.slug =slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form =PostForm()
    context ={
        'form':form
    }
    return render(request, 'dashboard/add_posts.html',context)

# for editing the post

def edit_posts(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form =PostForm(instance=post)
    if request.method =='POST':
        form =PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
        form=PostForm()

    context ={
        'form':form,
        'post':post,
    }
    
    return render(request, 'dashboard/edit_posts.html',context)

# for post deletion
def delete_posts(request,pk):
    post =get_object_or_404(BlogPost ,pk=pk)
    post.delete()
    return redirect('posts')

# crud operations for users
# 1. making users

def users(request):
    users = User.objects.all()
    context ={
        'users':users,
    }
    return render(request,'dashboard/users.html' ,context)

# 2. adding users

def add_users(request):
    form =UserForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form.save()
        return redirect('users')
    context ={
        'form':form,
    }
    return render(request,'dashboard/add_users.html',context)

#3. Edit users

def edit_users(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method =='POST':
        if form.is_valid(request.POST,instance=user):
            form.save()
            return redirect('users')
    form =EditForm(instance =user)

    context ={
        'form':form,
        'user':user,
    }
    return render(request,'dashboard/edit_users.html',context)

# 4. Delete User

def delete_users(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')