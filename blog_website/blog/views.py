from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import Post
from .forms import PostForm


# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='pub').order_by("-date_modified")
#
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


class PostListView(generic.ListView):
    # model = Post   age hame ro bekhaim hamin kafie va be def niaz nadarim
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):  # age bekhaim ye taghir ijad konim dige ino ezafe mikonim
        return Post.objects.filter(status='pub').order_by("-date_modified")


# def post_detail_view(request, pk):
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print("Excepted")
#     #     print()
#     # return render(request, 'blog/post_detail.html', {'post': post})
#
#     post = get_object_or_404(Post, pk=pk)
#
#     return render(request, 'blog/post_detail.html', {'post': post})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


def post_create_view(request):
    # # print(request.POST)
    # # print(request.POST.get('form-check-input'))
    # if request.method == "POST":
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     post_status = request.POST.get('status')
    #     print(post_title)
    #     user = User.objects.all()[0]
    #     if post_status == "on":
    #         st = "pub"
    #     else:
    #         st = "drf"
    #     Post.objects.create(title=post_title, text=post_text, author=user, status=st)
    # else:
    #     print("get request !")
    # return render(request, 'blog/post_create.html')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            # form = PostForm()
            return redirect('posts_list')
    else:  # get request
        form = PostForm()

    return render(request, 'blog/post_create.html', context={"form": form})


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#
#         return redirect('posts_list')
#     else:
#         print("bye")
#
#     return render(request, 'blog/post_update.html', context={"form": form, "post": post})


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_delete.html', context={"post": post})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

    # def get_success_url(self): vali majboor nistim intori beneviesim
    #     return reverse('posts_list')
