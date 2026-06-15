from django.urls import path

from . import views

urlpatterns = [
    # Dashboard URLs 
    path('', views.dashboard, name='dashboard'),
    path('Categories/', views.categories, name='categories'),
    path('Categories/add/', views.add_category, name='add_category'),
    path('Categories/edit/<int:pk>/',views.edit_category,name='edit_category'),
    path('Categories/delete/<int:pk>/',views.delete_category,name='delete_category'),

    # Posts URLs 
    path('posts/', views.posts , name='posts'),
    path('posts/add/', views.add_posts, name='add_posts'),
    path('posts/edit/<int:pk>/',views.edit_posts,name='edit_posts'),
    path('posts/delete/<int:pk>/',views.delete_posts,name='delete_posts'),

    # Users URls
    path('users/', views.users, name='users'),
    path('users/add/', views.add_users, name='add_users'),
    path('users/edit/<int:pk>/',views.edit_users,name='edit_users'),
    path('users/delete/<int:pk>/',views.delete_users,name='delete_users'),




]  