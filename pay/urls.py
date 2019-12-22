from django.conf.urls import url
from django.urls import path
from pay import views

app_name='pay'

urlpatterns=[
    path('hotel/<str:hotel>/<str:home>/',views.place_order,name='place_order'),
    url(r'^hotel/order',views.home_order,name='get_hotel'),
    path('attraction/<str:attraction>/',views.attraction_order,name='attraction_order'),
    url(r'^attraction/order',views.get_attraction,name='get_attraction'),
]