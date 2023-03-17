from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import logout


# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    context = {'blogPosts' : blogPostModel.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def createPost_view(request):

    context = {'form': blogPostForm}
    try:
        if request.method == 'POST':
            form = blogPostForm(request.POST)
            image = request.FILES['image']
            print(request.FILES)
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                description = form.cleaned_data['description']

            blogpost_obj = blogPostModel.objects.create(
                author=user, title=title,
                description=description, image=image
            )
            print(blogpost_obj)

            return redirect('/createpost/')
    except Exception as e:
        print(e)

    return render(request, 'create-post.html', context)


def deletePost_view(request, id):
    context = {}
    try:
        
        blogpost_obj = blogPostModel.objects.get(id = id)
        if blogpost_obj.author == request.user:
           blogpost_obj.delete()

        context['blogpost_obj'] = blogpost_obj
    except Exception as e:
        print(e)

    return redirect('/')


def updatePost_view(request, slug):
    context = {}
    try:

        blogpost_obj = blogPostModel.objects.get(slug = slug)
            
        if blogpost_obj.author != request.user:
                return redirect('/')
            
        inital_dict = {'description' : blogpost_obj.description}
        form = blogPostForm(initial=inital_dict)
           
        
        if request.method == 'POST':
            
            form = blogPostForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST['title']
            user = request.user

            if form.is_valid():
                print('Valid')
                description = form.cleaned_data['description']

            blogpost_obj = blogPostModel.objects.create(
                author=user, title=title,
                description=description, image=image
            )


        context['blogpost_obj'] = blogpost_obj
        context['form'] = form


    except Exception as e:
        print(e) 

    return render(request, 'update-post.html', context)