from django.conf.urls import url
from django.urls import path
from index import views

app_name = 'index'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),  # 首页路由
    url(r'^attractions/$', views.attractions, name='attractions'),  # 景区路由
    url(r'^hotel/$', views.hotel, name='hotel'),  # 酒店路由
    url(r'^news/$', views.news, name='news'),  # 新闻路由
    url(r'^flow/$', views.flow, name='flow'),  # 景区流量路由
    url(r'^login/$', views.login, name='login'),  # 登录路由
    url(r'^user_regist/$', views.regist, name='regist'),  # 用户注册路由
    url(r'^hotel_regist/$', views.hotel_regist, name='hotel_regist'),  # 酒店注册路由
    url(r'^attractions_regist/$', views.attractions_regist, name='attractions_regist'),  # 景区注册路由
    # 退出登录
    url(r'^sign_out/$', views.sign_out, name='sign_out'),

    # 个人中心路由
    url(r'^my_home/$', views.my_space, name='my_home'),  # 个人中心首页
    url(r'^change_password/$', views.change_password, name='change_password'),  # 修改密码
    url(r'^my_order/$', views.my_order, name='my_order'),  # 我的订单
    url(r'^change_information/$',views.change_information,name='change_information'), #修改信息
    url(r'^change/$',views.change,name='change'),  #修改密码请求

    # 酒店详情路由
    path('hotel/<str:datail>/', views.hotel_datail, name='hotel_datail'),
    # 景点详情路由

    path('attractions/<str:datail>/', views.attractions_datail, name='attractions_datail'),

    # 验证码路由
    url(r'index/$', views.verification, name='verification'),
    url(r'login/verification', views.verification),
    url(r'regist/verification', views.verification),
    url(r'^hotel_regist/verification', views.verification),
    url(r'^attractions_regist/verification', views.verification),
    url(r'^login_inspect/verification', views.verification),

    # 登录验证路由
    url(r'^login_inspect/$', views.login_inspect, name='login_inspect'),
    # 注册验证路由
    url(r'^regist_inspect/', views.regist_inspect, name='regist_inspect'),
    url(r'^attrations_inspect/', views.attractions_inspect, name='attractions_inspect'),
    url(r'^hotel_inspect/', views.hotel_inspect, name='hotel_inspect'),
]
