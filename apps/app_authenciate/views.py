import datetime
import time

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from celery import shared_task
from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.template import loader
from django.views.generic.base import View
from itsdangerous import URLSafeSerializer

from apps.app_authenciate.models import User
from .tasks import sendmail

# 登陆功能
from dj_authentication import settings


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证用户是否存在
        user = authenticate(request, username=username, password=password)
        if user:
            # 判断用户是否激活
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'msg': '用户尚未激活'})
        else:
            return render(request, 'login.html', {'msg': '用户密码错误'})


# 注册功能
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        try:
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')
            user = authenticate(username=username, password=password1)
            if user:
                # 用户已经存在
                return render(request, 'register.html', {'msg': '用户名已存在'})
            else:
                # 保存用户
                user = User.objects.create_user(username=username, password=password1, email=email,is_active=0)
                auth_s = URLSafeSerializer(settings.SECRET_KEY, "auth")
                token = auth_s.dumps({'name': username})
                cache.set(token,user.id,timeout=10 * 60)
                active_url= f'http://127.0.0.1:8000/active/?tooken={token}'
                content = loader.render_to_string('email.html',
                                                  request=request,
                                                  context={'username': username, 'active_url': active_url})
                sendmail.delay(content)
                return redirect('/')
        except Exception as e:
            return render(request, 'register.html', {'msg': '注册失败'})


#主页
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


#登出功能
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/login')


# 发送注册成功邮件，提醒激活



#点击激活链接，激活账号
def active(request):
    token=request.GET.get('tooken')
    uid=cache.get(token)
    if uid:
        User.objects.filter(id=uid).update(is_active=1)
        return redirect('/login')
    else:
        return redirect('/')




# def code(request):
#     if request.method == 'GET':
#         key = CaptchaStore.generate_key()
#         img_url = captcha_image_url(key)
#         return render(request, 'captcha.html', {'img_url': img_url, 'key': key})
#     else:
#         code = request.POST.get('code')
#         key = request.POST.get('key')
#         response = CaptchaStore.objects.filter(hashkey=key) .filter(expiration__lt=datetime.datetime.now())  .values('response').first().get('response')
#         if code.lower() == response:
#             pass
#         else:
#             key = CaptchaStore.generate_key()
#             img_url = captcha_image_url(key)
#
#
# def  refresh_code(request):
#     key = CaptchaStore.generate_key()
#     img_url = captcha_image_url(key)
#     return JsonResponse({'key':key,'img_url':img_url})