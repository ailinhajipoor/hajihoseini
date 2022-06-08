from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


# Create your views here.

def post_list_view(request):
    posts_list = Post.objects.all()

    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None
    #     print("Excepted")
    #     print()
    # return render(request, 'blog/post_detail.html', {'post': post})

    post = get_object_or_404(Post,pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})
