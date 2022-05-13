from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post, Group, User


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_posts.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    author_posts = Post.objects.filter(author=author)
    paginator = Paginator(author_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'paginator': paginator,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author_posts = Post.objects.filter(author=post.author)
    title = post.text[:30]
    context = {
        'post': post,
        'author_posts': author_posts,
        'title': title,
    }
    return render(request, 'posts/post_detail.html', context)





#TODO Разобраться с профайлом и пост деталями. Можно красивее!
#TODO Разобраться с тэмплейтами. Можно красивее!