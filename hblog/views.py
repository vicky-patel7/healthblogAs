from django.forms import DateTimeField
from django.http import Http404
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# index page
def index(request):
    allPosts = Post.objects.all()[:5]
    context = {'allPosts' : allPosts}
    return render(request, 'home/index.html', context)

# about page
def about(request):
    return render (request, 'home/about.html')


# user registration or signup
def signUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 12:
            messages.error(request, "Username must be less than 12 characters.")
            return redirect('index')
        if not username.isalnum():
            messages.error(request, "Username must contain letters and numbers")
            return redirect('index')
        if pass1 != pass2:
            messages.error(request, "Passwords didnot match")
            return redirect('index')

        myuser = User.objects.create_user(username = username, email = email, password = pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser = form.save(commit=False)
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('index')
    else:
        return HttpResponse("404 - NOT FOUND")

# user logout
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

# user login
def handleLogin(request):
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully loged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('index')
    else:
        return HttpResponse("404 - Not Found")



# all blog posts home
def blogPostsHome(request):
    allPosts = Post.objects.all() 
    context = {'allPosts' : allPosts}
    return render(request, 'myblog/blogHome.html', context)


# reading a single blog post
def blogPost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    post.views = post.views + 1
    post.save()
    print(post.image)
    context = {'post':post, 'user' : request.user}
    return render(request, 'myblog/blogPost.html', context)

# adding a new blog post to the database
def addNewBlogPost(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']
        slug = request.POST['slug']
        image = request.FILES.get('image')
        if len(author) == 0:
            messages.error(request, "Author name is required")
            return redirect('index')
        myNewPost = Post.objects.create(title = title, author = author, content = content, slug = slug, image = image)
        myNewPost.save()
        messages.success(request, "New Health Blog Post has been added.")
        return redirect('index')
    else:
        return HttpResponse("404 - NOT FOUND")