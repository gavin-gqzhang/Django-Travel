from django.conf.urls import url
from django.urls import path
from new import views
app_name='new'

urlpatterns=[
    # 旅游攻略路由
    path('', views.raiders, name='raiders'),  # 旅游攻略
    url(r'^raiders_search',views.raiders_search,name='raiders_search'),
    path('raiders/<str:distination>/<str:distance>/get_hotel', views.get_hotel, name='get_hotel'),
    path('raiders/<str:distination>/<str:distance>/get_attractions', views.get_attractions, name='get_attractions'),

    # 酒店后台路由
    url(r'^hotel_infor/',views.hotel_infor,name='hotel_infor'),          # 酒店信息提交
    path('hotel_backstage', views.hotel_index, name='hotel_backstage'),  # 酒店后台路由首页
    path('hotel_backtage/chart',views.hotel_chart,name='hotel_chart'),   # 酒店后台路由数据分析
    path('hotel_backtage/form',views.hotel_form,name='hotel_form'),   #    酒店后台路由酒店管理
    path('hotel_backtage/table',views.hotel_table,name='hotel_table'),   # 酒店后台路由酒店信息
    # 景区后台路由
    url(r'^attractions_infor/',views.attractions_infor,name='attractions_infor'),          # 景区信息提交
    path('attractions_backstage', views.attractions_index, name='attractions_backstage'),  # 景区后台路由首页
    path('attractions_backtage/chart', views.attractions_chart, name='attractions_chart'),  #景区后台路由数据分析
    path('attractions_backtage/form', views.attractions_form, name='attractions_form'),  #   景区后台路由景区管理
    path('attractions_backtage/table', views.attractions_table, name='attractions_table'),  #景区后台路由景区信息
]