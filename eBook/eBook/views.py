from django.shortcuts import render


def index(request):
    return render(request, 'Home\index.html')
