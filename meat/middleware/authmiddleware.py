from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect, JsonResponse


class AuthenticationMiddleware(MiddlewareMixin):
    """统一处理屏蔽掉匿名用户"""
    def process_request(self, request):
        if request.path == '/accounts/login/':
            return
        if not request.user.is_authenticated:
            if request.is_ajax():
                return JsonResponse({"code": 403, "message": "非法访问或登陆失效"})
            else:
                return HttpResponseRedirect("/accounts/login/?next="+request.path)
