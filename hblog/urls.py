from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('signup', views.signUp, name='signUp'),
    path('login', views.handleLogin, name='login'),
    path('logout', views.handleLogout, name='login'),
    path('blog', views.blogPostsHome, name='blogHome'),
    path('blog/add', views.addNewBlogPost, name='addNewBlogPost'),
    path('blog/<str:slug>', views.blogPost, name='blogPost'),
]
