from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

from django.contrib.auth.views import logout as sys_logout

from .modules import modules

def logout(request):
    sys_logout(request)
    return redirect(index)


def index(request):
    return render(request, 'index.html')


def nav(request):
    data = modules.copy()
    for parent in data:
        for child in parent["children"]:
            perm_name = '.'.join([child['label'], child['perimission']])
            child['display'] = request.user.has_perm(perm_name)
    return render(request, 'nav.html', {"modules": data})


def user_list(request):
    groups = Group.objects.all()
    return render(request, "user_list.html", {"groups": groups})


def get_users(request):
    users = User.objects.filter(is_superuser=False)
    ret = []
    for user in users:
        ret.append({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        })

    return JsonResponse({"code": 200, "data": ret})


def create_user(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    first_name = request.POST.get("first_name")
    group_id = request.POST.get("group")
    group = Group.objects.get(id=group_id)

    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = group.name
    user.save()
    user.groups.add(group_id)
    return JsonResponse({"code": 200, "message": "用户创建成功"})


def remove_user(request):
    pk = request.POST.get("id")
    user = User.objects.get(id=pk)
    user.delete()
    return JsonResponse({"code": 200, "message": "删除成功"})


def role_permission(request):
    roles = Group.objects.all()
    return render(request, 'permission.html', locals())



