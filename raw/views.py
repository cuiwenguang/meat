from django.shortcuts import render

from .models import RawConfig

def create(request):
    return render(request, 'raw/create.html')


def config(request):
    config = RawConfig.objects.first()
    return render(request, 'raw/config.html', {"config":config})


def raw_list(request):
    return render(request, 'raw/list.html')


def collect_create(request):
    config = RawConfig.objects.first()
    return render(request, 'raw/collect_create.html', {"config":config})