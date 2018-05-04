from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout as sys_logout

from .modules import modules

def logout(request):
    sys_logout(request)
    return redirect(index)


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def nav(request):
    return render(request, 'nav.html', {"modules": modules})