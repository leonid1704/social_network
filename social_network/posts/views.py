from django.http import HttpResponse


def index(request):
    return HttpResponse('This is Start Page')


def group_posts(request, slug):
    return HttpResponse(f'You type slug {slug}')
