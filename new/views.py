import hashlib
import os
import calendar
from urllib import parse  # 经纬度转化
from math import radians, cos, sin, asin, sqrt, pi, fabs
import requests
import json
import matplotlib
import matplotlib.pyplot
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from Travels import settings
from index.models import *
from django.urls import reverse


# Create your views here.

# 旅游攻略
def raiders(request):
    if request.session.get('username'):
        login=request.session.get('username')
    else:
        login=None
    context={
        'username':login,
    }
    return render(request, 'raiders.html',context=context)


# 旅游攻略搜索回显
def raiders_search(request):
    if request.POST:
        distination=request.POST['distination']
        distance=request.POST['distance']
        print(distance)
        print(distination)

    context={
        'distination':distination,
        'distance':distance,
        }
    return render(request, 'raiders_search.html',context=context)


# 旅游攻略获取酒店信息
def get_hotel(request,distination,distance):
    ctx={}
    hotels=[]
    print(distination)
    print(distance)
    hotel_datail=HotelDatail.objects.all()
    ctx['lng1']=address(distination)['lng']
    ctx['lat1']=address(distination)['lat']
    for hotel in hotel_datail:
        ctx['lng2']=address(hotel.address)['lng']
        ctx['lat2']=address(hotel.address)['lat']
        d=get_distance_hav(ctx['lat1'], ctx['lng1'], ctx['lat2'], ctx['lng2'])
        if float(d)<=float(distance):
            hotels.append(hotel)

    context={
        'hotels':hotels,
    }
    return render(request, 'raiders_hotel.html',context=context)


# 旅游攻略获取景区信息
def get_attractions(request,distination,distance):
    ctx = {}
    attractions = []
    attractions_datail = AttractionsDatail.objects.all()
    ctx['lng1'] = address(distination)['lng']
    ctx['lat1'] = address(distination)['lat']
    for attraction in attractions_datail:
        ctx['lng2'] = address(attraction.address)['lng']
        ctx['lat2'] = address(attraction.address)['lat']
        d = get_distance_hav(ctx['lat1'], ctx['lng1'], ctx['lat2'], ctx['lng2'])
        if float(d) <= float(distance):
            attractions.append(attraction)

    context = {
        'attractions':attractions,
        'public':PublicityPhoto.objects.all()
    }

    return render(request, 'raiders_attractions.html',context=context)


# 酒店后台首页
def hotel_index(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = AuthUser.objects.get(username=username)
        hotel_id = user.hotel_user
        hotel_datail=HotelDatail.objects.get(id=hotel_id)
        orders = HotelOrder.objects.filter(hotel_id=hotel_id)
        now = timezone.localdate()
        len_order = len(orders)
        today_order = 0
        today_price=0
        sum_price=0
        sal_home=0
        persons=0

        for order in orders:
            sal_home=sal_home+1
            sum_price = sum_price + order.price
            time = order.auth_time
            time = time.strftime('%Y-%m-%d')
            if str(time)==str(now):
                persons = int(persons) + int(order.person)
                today_price = today_price + order.price
                today_order = today_order + 1

        hotel_order=HotelOrder.objects.filter(hotel_id=hotel_id)
        home_datail=HomeDatail.objects.filter(hotel_id=hotel_id)

        context = {
            'username': username,
            'sum_order': len_order,
            'today_order': today_order,
            'sum_price':sum_price,
            'today_price':today_price,
            'sal_home':sal_home,
            'persons':persons,
            'home_datail':home_datail,
            'hotel_datail':hotel_datail,
        }

        return render(request, 'hotel_backstage/index.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))


# 酒店后台数据分析
def hotel_chart(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = AuthUser.objects.get(username=username)
        hotel_id = user.hotel_user
        orders = HotelOrder.objects.filter(hotel_id=hotel_id)
        now = timezone.localdate()
        len_order = len(orders)
        today_order = 0
        for order in orders:
            time = order.auth_time
            time = time.strftime('%Y-%m-%d')
            if str(time)==str(now):
                today_order = today_order + 1

        context = {
            'username': username,
            'sum_order': len_order,
            'today_order': today_order,
        }
        return render(request, 'hotel_backstage/chart.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))


# 酒店后台酒店管理
def hotel_form(request):
    if request.session.get('username'):
        username=request.session.get('username')
        user=AuthUser.objects.get(username=username)
        hotel_datail=HotelDatail.objects.get(id=user.hotel_user)
        manager=hotel_datail.manager
        name=hotel_datail.name
        max_price=hotel_datail.max_price
        min_price=hotel_datail.min_price
        address=hotel_datail.address
        phone=hotel_datail.phone
        email=hotel_datail.email
        in_time=hotel_datail.in_time
        home_num=hotel_datail.home_num
        now=timezone.localdate()
        hotel_id=user.hotel_user
        orders=HotelOrder.objects.filter(hotel_id=hotel_id)
        len_order=len(orders)
        today_order=0
        for order in orders:
            time=order.auth_time
            time=time.strftime('%Y-%m-%d')
            if str(time)==str(now):
                today_order=today_order+1


        context={
            'username':username,
            'manager':manager,
            'name':name,
            'max_price':max_price,
            'min_price':min_price,
            'address':address,
            'phone':phone,
            'email':email,
            'in_time':in_time,
            'home_num':home_num,
            'sum_order':len_order,
            'today_order':today_order,
        }

        return render(request, 'hotel_backstage/form.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))



# 酒店后台信息管理
def hotel_table(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = AuthUser.objects.get(username=username)
        hotel_id = user.hotel_user
        orders = HotelOrder.objects.filter(hotel_id=hotel_id)
        now = timezone.localdate()
        len_order = len(orders)
        today_order = 0
        today_price=0
        sum_price=0
        today_order_datail=[]
        for order in orders:
            sum_price=sum_price+order.price
            time = order.auth_time
            time = time.strftime('%Y-%m-%d')
            if str(time)==str(now):
                today_order = today_order + 1
                today_price=today_price+order.price
                today_order_datail.append(order)

        hotel_order=HotelOrder.objects.filter(hotel_id=hotel_id)
        home_datail=HomeDatail.objects.filter(hotel_id=hotel_id)

        #获取当前月以及天数
        year=timezone.localdate().strftime('%Y')
        mouth=timezone.localdate().strftime('%m')
        day=calendar.monthrange(int(year), int(mouth))[1]

        date=[]
        for i in range(1,day+1):
            today=('{}-{}-{}').format(year,mouth,i)
            date.append(today)

        print(date)

        context={
            'username':username,
            'sum_order':len_order,
            'today_order':today_order,
            'hotel_order':hotel_order,
            'home_datail':home_datail,
            'sum_price':sum_price,
            'today_price':today_price,
            'today_order_datail':today_order_datail,
            'date':date,
        }

        return render(request, 'hotel_backstage/table.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))



# 酒店信息提交
def hotel_infor(request):
    global publicity_photo, manager, hotel_name, address, max_price, min_price, datail, phone, email, home_num, in_time, home_img, home_name, person, home_price, num
    if request.session.get('username'):
        pass
    else:
        return redirect(reverse(
            "home:login"
        ))
    if request.POST:
        manager = request.POST['username']
        hotel_name = request.POST['hotel_name']
        address = request.POST['address']
        phone = request.POST['phone']
        home_num = request.POST['home_num']
        email = request.POST['email']
        in_time = request.POST['in_time']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        datail = request.POST['editor1']
        home_name = request.POST.getlist('home')
        home_price = request.POST.getlist('price')
        home_details = request.POST.getlist('home_detail')
        home_img=request.FILES.getlist('img')
        person = request.POST.getlist('person')
        num = request.POST.getlist('num')
        publicity_photo = request.FILES.get('Publicity_photo')

        try:
            min_price=float(min_price)
        except:
            min_price=0.0
        try:
            max_price=float(max_price)
        except:
            max_price=0.0
        try:
            home_num=int(home_num)
        except:
            home_num=0

    # 信息存储数据库中
    user = request.session.get('username')
    try:
        hotel_id = AuthUser.objects.get(username=user).hotel_user
        hotel_datail = HotelDatail.objects.get(id=hotel_id)
        hotel_datail.manager = manager
        hotel_datail.name = hotel_name
        hotel_datail.address = address
        hotel_datail.max_price = max_price
        hotel_datail.min_price = min_price
        hotel_datail.datail = datail
        hotel_datail.phone = phone
        hotel_datail.email = email
        hotel_datail.home_num = home_num
        hotel_datail.in_time = in_time
        hotel_datail.save()
    except AuthUser.DoesNotExist:
        hotel_datail = HotelDatail(
            manager=manager,
            name=hotel_name,
            max_price=max_price,
            min_price=min_price,
            datail=datail,
            address=address,
            phone=phone,
            home_num=home_num,
            email=email,
            in_time=in_time,
        )
        hotel_datail.save()
        hotel_id = hotel_datail.id
        auth_user = AuthUser.objects.get(username=user)
        auth_user.hotel_user = hotel_id
        auth_user.save()

    #   图片存储
    for i in range(len(home_name)):
        if len(home_img)!=0:
            if home_img[i]!="":
                path = os.path.join(settings.MEDIA_ROOT, 'hotel', hotel_name, home_name[i])
                if not os.path.exists(path):
                    os.makedirs(path)
                url = os.path.join(path, home_img[i].name)
                with open(url, 'wb') as save_file:
                    for part in home_img[i].chunks():
                        save_file.write(part)
                        save_file.flush()
                if HomeDatail.objects.filter(home=home_name[i]):
                    refresh = HomeDatail.objects.get(home=home_name[i])
                    refresh.hotel_id = hotel_id
                    refresh.home = home_name[i]
                    refresh.person_num = person[i]
                    refresh.price = home_price
                    refresh.num = num[i]
                    refresh.datail = home_details[i]
                    refresh.save()
                    home_id = refresh.id
                    hotel_img = HotelImg.objects.get(hotel_id=hotel_id)
                    hotel_img.home_id = home_id,
                    hotel_img.img = os.path.join(
                        'hotel', hotel_name, home_name[i], home_img[i].name
                    )
                else:
                    home_datail = HomeDatail(
                        hotel_id=hotel_id,
                        home=home_name[i],
                        person_num=person[i],
                        price=home_price[i],
                        num=num[i],
                        datail=home_details[i],
                    )
                    home_datail.save()
                    home_id = home_datail.id
                    hotel_img = HotelImg(
                        hotel_id=hotel_id,
                        home_id=home_id,
                        img=os.path.join(
                            'hotel', hotel_name, home_name[i], home_img[i].name
                        )
                    )
        else:
            if home_name[i]!="" and person[i]!="" and num[i]!="" and home_price[i]!="":
                if HomeDatail.objects.filter(home=home_name[i]):
                    refresh = HomeDatail.objects.get(home=home_name[i])
                    refresh.hotel_id = hotel_id
                    refresh.home = home_name[i]
                    refresh.person_num = person[i]
                    refresh.price = home_price[i]
                    refresh.num = num[i]
                    refresh.datail = home_details[i]
                    refresh.save()
                else:
                    home_datail = HomeDatail(
                        hotel_id=hotel_id,
                        home=home_name[i],
                        person_num=person[i],
                        price=home_price[i],
                        num=num[i],
                        datail=home_details[i],
                    )
                    home_datail.save()
            else:
                pass
    # 宣传照存储
    if publicity_photo != None:
        path = os.path.join(settings.MEDIA_ROOT, 'hotel', hotel_name, 'publicity_photo')
        if not os.path.exists(path):
            os.makedirs(path)
        url = os.path.join(path, publicity_photo.name)
        with open(url, 'wb') as  save_file:
            for part in publicity_photo.chunks():
                save_file.write(part)
                save_file.flush()
        if PublicityPhoto.objects.filter(hotel_id=hotel_id):
            refresh = PublicityPhoto.objects.get(hotel_id=hotel_id)
            refresh.upload = os.path.join(
                'hotel', hotel_name, 'publicity_photo', publicity_photo.name
            )
            refresh.save()
        else:
            image = PublicityPhoto(
                hotel_id=hotel_id,
                upload=os.path.join(
                    'hotel', hotel_name, publicity_photo.name
                )
            )
            image.save()
    else:
        pass

    return redirect(reverse('my_space:hotel_backstage'))# 127.0.0.1:8000/my_space/hotel_backstage


# 景区后台首页
def attractions_index(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = AuthUser.objects.get(username=username)
        attractions_id = user.attractions_user
        orders = AttractionsOrder.objects.filter(attractions_id=attractions_id)
        now = timezone.localdate()
        len_order = len(orders)
        today_order = 0
        today_price=0
        sum_price=0
        for order in orders:
            sum_price=sum_price+order.price
            time = order.auth_time
            time = time.strftime('%Y-%m-%d')
            if str(time) == str(now):
                today_price=today_price+order.price
                today_order = today_order + 1
        attractions_datatil=AttractionsDatail.objects.get(id=attractions_id)
        attractions_price=AttractionsPrice.objects.filter(name_id=attractions_id)

        context = {
            'username': username,
            'sum_order': len_order,
            'today_order': today_order,
            'today_price':today_price,
            'sum_price':sum_price,
            'attraction_datail':attractions_datatil,
            'attraction_price':attractions_price,
        }
        return render(request, 'attractions_backstage/index.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))


# 景区后台数据分析
def attractions_chart(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = AuthUser.objects.get(username=username)
        attractions_id = user.attractions_user
        orders = AttractionsOrder.objects.filter(attractions_id=attractions_id)
        now = timezone.localdate()
        len_order = len(orders)
        today_order = 0
        for order in orders:
            time = order.auth_time
            time = time.strftime('%Y-%m-%d')
            if str(time) == str(now):
                today_order = today_order + 1

        context = {
            'username': username,
            'sum_order': len_order,
            'today_order': today_order,
        }
        return render(request, 'attractions_backstage/chart.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))



# 景区后台景区管理
def attractions_form(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = AuthUser.objects.get(username=username)
        attractions_id = user.attractions_user
        orders = AttractionsOrder.objects.filter(attractions_id=attractions_id)
        now = timezone.localdate()
        len_order = len(orders)
        today_order = 0
        for order in orders:
            time = order.auth_time
            time = time.strftime('%Y-%m-%d')
            if str(time) == str(now):
                today_order = today_order + 1
        attractions_datail=AttractionsDatail.objects.get(id=attractions_id)

        try:
            flow = Flow.objects.get(name_id=attractions_id)
        except:
            flow={
                'time1_flow':'',
                'time2_flow':'',
                'time3_flow':'',
                'time4_flow':'',
                'time5_flow':'',
                'time6_flow':'',
            }

        context = {
            'username': username,
            'sum_order': len_order,
            'today_order': today_order,
            'attractions_datail':attractions_datail,
            'flow':flow,
        }
        return render(request, 'attractions_backstage/form.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))


# 景区后台信息管理
def attractions_table(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = AuthUser.objects.get(username=username)
        attractions_id = user.attractions_user
        orders = AttractionsOrder.objects.filter(attractions_id=attractions_id)
        now = timezone.localdate()
        len_order = len(orders)
        today_order = 0
        today_price=0
        sum_price=0
        today_orders=[]
        for order in orders:
            sum_price = sum_price + order.price
            time = order.auth_time
            time = time.strftime('%Y-%m-%d')
            if str(time) == str(now):
                today_orders.append(order)
                today_price = today_price + order.price
                today_order = today_order + 1
                print(order.auth_time)
        attractions_price=AttractionsPrice.objects.filter(name_id=attractions_id)
        attractions_datail=AttractionsDatail.objects.get(id=attractions_id)

        # 获取当前月以及天数
        year = timezone.localdate().strftime('%Y')
        mouth = timezone.localdate().strftime('%m')
        day=timezone.localdate().strftime('%d')
        # day = calendar.monthrange(int(year), int(mouth))[1]

        date = []
        for i in range(1, int(day) + 1):
            today = ('{}-{}-{}').format(year, mouth, i)
            date.append(today)
        print(date)
        context = {
            'attraction_price':attractions_price,
            'attraction_datail':attractions_datail,
            'orders':orders,
            'today_orders':today_orders,
            'username': username,
            'sum_order': len_order,
            'today_order': today_order,
            'today_price': today_price,
            'sum_price': sum_price,
            'date':date,
        }
        return render(request, 'attractions_backstage/table.html',context=context)
    else:
        return redirect(reverse(
            "home:login"
        ))



# 景区后台信息提交
def attractions_infor(request):
    global publicity_photo, attractions_name, address, phone, username, max_num, max_price, min_price, datail, email, type, in_time, ticket_name, ticket_price, img
    if request.session.get('username'):
        pass
    else:
        return redirect(reverse(
            "home:login"
        ))
    if request.POST:
        username = request.POST['username']
        attractions_name = request.POST['attractions_name']
        address = request.POST['address']
        phone = request.POST['phone']
        type = request.POST['type']
        max_num = request.POST['max_num']
        email = request.POST['email']
        in_time = request.POST['in_time']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        datail = request.POST['editor1']
        ticket_name = request.POST.getlist('home')
        ticket_price = request.POST.getlist('price')
        img = request.FILES.getlist('img')
        publicity_photo = request.FILES.get('publicity_photo')
        time1=request.POST['time1']
        time2=request.POST['time2']
        time3=request.POST['time3']
        time4=request.POST['time4']
        time5=request.POST['time5']
        time6=request.POST['time6']
        try:
            max_num=int(max_num)
        except:
            max_num=100
        try:
            max_price=float(max_price)
        except:
            max_price=0
        try:
            min_price=float(min_price)
        except:
            min_price=0
        try:
            time1=float(time1)
        except:
            time1=0.0
        try:
            time2 = float(time2)
        except:
            time2 = 0.0
        try:
            time3 = float(time3)
        except:
            time3 = 0.0
        try:
            time4 = float(time4)
        except:
            time4 = 0.0
        try:
            time5 = float(time5)
        except:
            time5 = 0.0
        try:
            time6 = float(time6)
        except:
            time6 = 0.0

    #生成流量图
    times=[time1,time2,time3,time4,time5,time6]
    url=flow_index_line(names=['第一个月','第二个月','第三个月','第四个月','第五个月','第六个月'],y=times,title=attractions_name,max=max_num)
    # url_line=flow_index(names=['第一个月','第二个月','第三个月','第四个月','第五个月','第六个月'],y=times,title=attractions_name,max=max_num)

    #  信息存储
    user = request.session.get('username')
    try:
        attractions_id = AuthUser.objects.get(username=user).attractions_user
        attractions_datail = AttractionsDatail.objects.get(id=attractions_id)
        attractions_datail.name = attractions_name
        attractions_datail.address = address
        attractions_datail.phone = phone
        attractions_datail.manager = username
        attractions_datail.max_num = int(max_num)
        attractions_datail.max_price = max_price
        attractions_datail.min_price = min_price
        attractions_datail.datail = datail
        attractions_datail.email = email
        attractions_datail.type = type
        attractions_datail.in_time = in_time
        attractions_datail.save()
    except:
        print("景区详情信息修改出现异常")
        attractions_datail = AttractionsDatail(
            name=attractions_name,
            manager=username,
            address=address,
            phone=phone,
            max_num=int(max_num),
            max_price=max_price,
            min_price=min_price,
            datail=datail,
            email=email,
            type=type,
            in_time=in_time
        )
        attractions_datail.save()
        attractions_id = attractions_datail.id
        auth_user = AuthUser.objects.get(username=user)
        auth_user.attractions_user = attractions_id
        auth_user.save()

    try:
        flow=Flow.objects.get(name_id=attractions_id)
        flow.time1_flow=time1
        flow.time2_flow=time2
        flow.time3_flow=time3
        flow.time4_flow=time4
        flow.time5_flow=time5
        flow.time6_flow=time6
        flow.max=max_num
        flow.flow_img=url
        flow.save()

    except:
        print("流量数据信息修改出现异常")
        flow=Flow(
            name_id=attractions_datail.id,
            time1_flow=time1,
            time2_flow=time2,
            time3_flow=time3,
            time4_flow=time4,
            time5_flow=time5,
            time6_flow=time6,
            max=max_num,
            flow_img=url,
        )
        flow.save()



    for i in range(0, len(ticket_name)):
        if ticket_name[i]=='':
            pass
        else:
            try:
                attractions_price=AttractionsPrice.objects.get(name_id=attractions_id)
                attractions_price.ticket_name=ticket_name[i]
                attractions_price.ticket_price=ticket_price[i]
                attractions_price.save()
            except:
                attractions_price = AttractionsPrice(
                    name_id=attractions_id,
                    ticket_name=ticket_name[i],
                    ticket_price=ticket_price[i],
                )
                attractions_price.save()


    #   图片存储
    for i in range(0, len(img)):
        if img[i]!='':
            path = os.path.join(settings.MEDIA_ROOT, 'attractions', attractions_name)
            if not os.path.exists(path):
                os.makedirs(path)
            url = os.path.join(path, img[i].name)
            with open(url, 'wb') as save_file:
                for part in img[i].chunks():
                    save_file.write(part)
                    save_file.flush()
            attractions_img = AttractionsImg(
                attractions_id=attractions_id,
                img=os.path.join(
                    'attractions', attractions_name, img[i].name
                )
            )
            attractions_img.save()
        else:
            pass
    # 宣传照存储
    if publicity_photo!=None:
        path = os.path.join(settings.MEDIA_ROOT, 'attractions', attractions_name,'publicity_photo')
        if not os.path.exists(path):
            os.makedirs(path)
        url = os.path.join(path, publicity_photo.name)
        with open(url, 'wb') as save_file:
            for part in publicity_photo.chunks():
                save_file.write(part)
                save_file.flush()
        try:
            image=PublicityPhoto.objects.get(attractions_id=attractions_id)
            image.upload=os.path.join(
                    'attractions', attractions_name, 'publicity_photo',publicity_photo.name
                )
            image.save()
        except:
            image = PublicityPhoto(
                attractions_id=attractions_id,
                upload=os.path.join(
                    'attractions', attractions_name, 'publicity_photo',publicity_photo.name
                )
            )
            image.save()
    else:
        pass
    return redirect(reverse('my_space:attractions_backstage'))

'''
    画图
'''
def flow_index_line(names, y,max, title):
    x = range(len(names))
    plt = matplotlib.pyplot
    plt.cla()
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    for i in range(len(y)):
        try:
            y[i] = float(y[i])
        except:
            y[i]=0
    plt.plot(x, y, marker='o', mec='r', mfc='w', label=u'flow')
    plt.legend()  # 让图例生效
    plt.xticks(x, names, rotation=45)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.ylim(0,float(max))
    plt.xlabel(u"日期")  # x轴标签
    plt.ylabel("流量")  # y轴标签
    plt.title(title + "风景区")  # 标题
    plt.savefig('media/FlowImg/' + title + '_line.jpg')
    url=('FlowImg/{}_line.jpg'.format(title))
    return url

def flow_index(names,y,max,title):
    plt=matplotlib.pyplot
    color=['r','b','g']
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel('日期')
    plt.ylabel('流量 (k)')
    plt.title(title+"风景区")
    for i in range(len(names)):
        y[i]=float(y[i])
        plt.bar(names[i],y[i],label=names[i],width=0.45)
    plt.ylim(0,float(max))
    plt.legend()
    plt.savefig('media/FlowImg/' + title + '.jpg')
    url = ('FlowImg/{}.jpg'.format(title))
    return url


#    两点键位置信息具体测定   #
EARTH_RADIUS = 6371  # 地球平均半径，6371km
#      对输入的两个经纬度信息进行测距   #
def hav(theta):
    s = sin(theta / 2)
    return s * s
def get_distance_hav(lat0, lng0, lat1, lng1):
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
    return distance
#     获取详细地址的经纬度信息函数        #
def address(address):
    address_index = {}
    queryStr = '/geocoder/v2/?address=%s&output=json&ak=leDOPGBU5Gwk6D3wGZigrNk560zN50GX' % address
    encodeStr = parse.quote(queryStr, safe="/:=&?#+!$,;@'()*[]")
    rawStr = encodeStr + 'leDOPGBU5Gwk6D3wGZigrNk560zN50GX'
    sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())
    url = parse.quote("http://api.map.baidu.com" + queryStr + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
    res = requests.get(url)
    json_data = json.loads(res.text)
    longitude = json_data['result']['location']['lng']  # 经度
    latitude = json_data['result']['location']['lat']  # 纬度
    address_index['lng'] = longitude
    address_index['lat'] = latitude
    return address_index  # 返回携带具体经纬度信息的字典