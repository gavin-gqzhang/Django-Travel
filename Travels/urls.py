"""Travels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url

#  设置media可被访问
from django.conf import settings
from django.views.static import serve

from django.contrib import admin
from django.urls import path, include
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 富文本文件上传
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home),
    path('', include(('index.urls', 'index'), namespace='home')),  # 定义首页路由
    path('my_space/', include(('new.urls', 'new'), namespace='my_space')),  # 定义个人中心路由
    path('pay/', include(('pay.urls', 'pay'), namespace='pay')),  # 定义支付路由
    path('raiders/',include(('new.urls','new'),namespace='raiders')),   # 定义旅游攻略
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 定义media路径
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS}),  # 定义static路径

    path('verification/', include(('index.urls','index'),namespace='verification')),  # 验证码路由
]
