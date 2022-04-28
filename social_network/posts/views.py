from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_posts.html'
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'title': title
    }
    return render(request, template, context)
