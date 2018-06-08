from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
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
    id = request.POST.get("id")
    if int(id) == 0:
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
    else:
        user = User.objects.get(id=id)
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        group_id = request.POST.get("group")
        group = Group.objects.get(id=group_id)
        user.last_name = group.name
        user.save()
        return JsonResponse({"code": 300, "mess":"修改成功"})


def edit_user(request):
    id = request.POST.get("id")
    user = User.objects.filter(is_superuser=False, id=id)
    ret = []
    for u in user:
        ret.append({
            "id": u.id,
            "username": u.username,
            "password": u.password,
            "first_name": u.first_name,
            "last_name": u.last_name,
            "email": u.email,
        })
    return JsonResponse({"code": 200, "data": ret})


def remove_user(request):
    pk = request.GET.get("id")
    user = User.objects.get(id=pk)
    user.delete()
    return JsonResponse({"code": 200, "message": "删除成功"})


def role_permission(request):
    roles = Group.objects.all()
    return render(request, 'permission.html', locals())


def role_list(request):
    return render(request, "role_list.html")


def get_role(request):
    group = Group.objects.all()
    ret = []
    for g in group:
        ret.append({
            "id": g.id,
            "name": g.name,
        })
    return JsonResponse({"code": 200, "data": ret})


def create_role(request):
    id = request.POST.get("id")
    print(id)
    if int(id) == 0:
        name = request.POST.get("name")
        role = Group.objects.create(name=name)
        role.save()
        return JsonResponse({"code": 200, "message": "用户创建成功"})
    else:
        group = Group.objects.get(id=id)
        print(group.id, group.name)
        name = request.POST.get("name")
        group.name = name
        group.save()
        return JsonResponse({"code": 300, "mess": "修改成功"})


def edit_role(request):
    id = request.GET.get("id")
    group = Group.objects.get(id=id)
    name = group.name
    return JsonResponse({"code": 200, "data": name})


def remove_role(request):
    id= request.GET.get("id")
    group = Group.objects.get(id=id)
    group.delete()
    return JsonResponse({"code": 200, "mess": "删除成功"})


def power_resp(request):
    id = request.GET.get("id")
    group = Group.objects.get(id=id)
    perms = [p for p in group.permissions.all()]
    return render(request, 'power_resp.html', {"group": group, "perms": perms})


def get_perms(request):
    from django.contrib.auth.models import Permission
    perms = Permission.objects.filter(content_type__id__gte=7).values('id', 'name')
    ret = []
    for p in perms:
        ret.append({
            "id": p["id"],
            "name": p["name"],
        })
    return JsonResponse({"code": 200, "data": ret})


def update_perms(request):
    id = request.GET.get("id")
    group = Group.objects.get(id=id)
    print(group)
    perms = request.GET.getlist("perm[]")
    print(perms)
    group.permissions.clear()
    group.permissions.add(*perms)
    return JsonResponse({"code": 200})


def change_password(request):
    old_psd = request.POST.get("psd")
    rePsd = request.POST.get("rePsd")
    print(rePsd)
    username = request.user
    user = authenticate(username=username, password=old_psd)
    print(user)
    if user:
        user.password = make_password(rePsd)
        user.save()
        return JsonResponse({"code": 200, "mess": "修改成功，本次退出后生效"})
    else:
        return JsonResponse({"mess": "密码输入错误"})