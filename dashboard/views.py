from django.shortcuts import redirect, render ,get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Category ,BlogPost
from dashboard.form import CategoryForm

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
