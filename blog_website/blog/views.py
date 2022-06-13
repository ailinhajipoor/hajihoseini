from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Create your views here.

def post_list_view(request):
    # posts_list = Post.objects.all()
    posts_list = Post.objects.filter(status='pub')

    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None
    #     print("Excepted")
    #     print()
    # return render(request, 'blog/post_detail.html', {'post': post})

    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    # print(request.POST)
    # print(request.POST.get('form-check-input'))
    if request.method == "POST":
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')
        post_status = request.POST.get('status')
        print(post_title)
        user = User.objects.all()[0]
        if post_status == "on":
            st = "pub"
        else:
            st = "drf"
        Post.objects.create(title=post_title, text=post_text, author=user, status=st)
    else:
        print("get request !")
    return render(request, 'blog/post_create.html')
