from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def news(request):
    return HttpResponse("<h1>Nowości u studentów</h1>")
    # return render(request, 'pizza/news.html')
