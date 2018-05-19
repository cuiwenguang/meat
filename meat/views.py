from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout as sys_logout

from .modules import modules

def logout(request):
    sys_logout(request)
    return redirect(index)


@login_required
def index(request):
    return render(request, 'index.html')


def nav(request):
    return render(request, 'nav.html', {"modules": modules})


def user_list(request):
    return render(request, "user_list.html")


def get_users(request):
    users = User.objects.filter(is_superuser=False)
    ret = []
    for user in users:
        ret.append({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "emial": user.email,
        })

    return JsonResponse({"code": 200, "data": ret})


def create_user(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")

    user = User()
    User.objects.create(username=username,email=email,
                        password=password, first_name=first_name,
                        last_name=last_name)

    return JsonResponse({"code": 200, "message": "用户创建成功"})


