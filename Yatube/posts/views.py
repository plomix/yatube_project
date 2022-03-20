from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Yatube Главная')

def groups_posts(request, slug):
    return HttpResponse(f'Yatube POST {slug}')
