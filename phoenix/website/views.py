from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "auth/login.html")


def register(request):
    return render(request, "auth/register.html")
