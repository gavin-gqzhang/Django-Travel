from django.conf.urls import url
from django.urls import path
from pay import views

app_name='pay'

urlpatterns=[
    path('hotel/<str:hotel>/<str:home>/',views.place_order,name='place_order'),#预订酒店房间页面
    url(r'^hotel/order',views.home_order,name='get_hotel'),#提交预订
    path('attraction/<str:attraction>/',views.attraction_order,name='attraction_order'),#景区门票预订
    url(r'^attraction/order',views.get_attraction,name='get_attraction'),#门票预订提交
]