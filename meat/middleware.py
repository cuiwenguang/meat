from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.http.response import JsonResponse

class AuthMiddleware(MiddlewareMixin):
    """权限认证中间件"""

    def process_request(self, request):
        if request.user is None:
            if request.is_ajax():
                return JsonResponse({"code":401, "message": "未授权或者登陆超时"})
            else:
                redirect('/accounts/login')

        return None

    def process_response(self, request, response):
        return response