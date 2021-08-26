from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(form)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    # Show
    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):
    # Find Post
    post = Post.objects.get(id=post_id)
# if item select delete it will delete the post
    post.delete()
    return HttpResponseRedirect('/')


def update(request, post_id):
    # If the method is POST
    post = Post.objects.get(id=post_id)

    # if request file is there return tweets
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # save and reddirect to home page
            return HttpResponseRedirect('/')
    # if we want to update then it will redirect back to the update.html it will display to user
    else:
        form = PostForm
        return render(request, 'update.html', {'post': post, 'form': form})


def like(request, post_id):
    # Find Post
    post = Post.objects.get(id=post_id)
    newlikecount = post.like_count+1
    post.like_count = newlikecount
    post.save()
    return HttpResponseRedirect('/')
