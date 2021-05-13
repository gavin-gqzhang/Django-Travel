from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect
from PIL import Image, ImageDraw, ImageFont
import random
from index.models import *
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.hashers import make_password,check_password
from index.models import *
import hashlib
import re
import os
# Create your views here.

'''
    功能性方法
'''
def get_img():
    f=open('E:\python-web\Django-Travel\static\index\css\open-iconic-bootstrap.min.css','a+')
    f.seek(0)
    for i in f:
        img=i
    all_img=re.findall('.oi-(\w*):b',img)
    return all_img

# 首页
def home(request):
    myspace=0
    attraction_user=0
    hotel_user=0
    if request.session.get('username'):
        login=request.session.get('username')
        user = AuthUser.objects.get(username=login)
        if user.attractions_user == 0 and user.hotel_user == 0:
            myspace = 1
        if user.attractions_user != 0 and user.hotel_user == 0:
            attraction_user = 1
        if user.attractions_user == 0 and user.hotel_user != 0:
            hotel_user = 1
    else:
        login=None



    # 携带数据传输
    context={
        'hotel_datail':HotelDatail.objects.all(),
        'attractions_datail':AttractionsDatail.objects.all(),
        'attractions_img':AttractionsImg.objects.all(),
        'publicity_photo': PublicityPhoto.objects.all(),
        'username':login,
        'myspace':myspace,
        'attraction_user':attraction_user,
        'hotel_user':hotel_user,
        'beautiful':get_img(),
    }
    return render(request, 'index.html',context=context)


# 景点
def attractions(request):
    myspace = 0
    attraction_user = 0
    hotel_user = 0
    if request.session.get('username'):
        login = request.session.get('username')
        user = AuthUser.objects.get(username=login)
        if user.attractions_user == 0 and user.hotel_user == 0:
            myspace = 1
        if user.attractions_user != 0 and user.hotel_user == 0:
            attraction_user = 1
        if user.attractions_user == 0 and user.hotel_user != 0:
            hotel_user = 1
    else:
        login = None
    # 携带数据传输
    context = {
        'hotel_datail': HotelDatail.objects.all(),
        'attractions_datail': AttractionsDatail.objects.all(),
        'attractions_img': AttractionsImg.objects.all(),
        'publicity_photo': PublicityPhoto.objects.all(),
        'username': login,
        'myspace': myspace,
        'attraction_user': attraction_user,
        'hotel_user': hotel_user,
        'beautiful': get_img(),
    }
    return render(request, 'templates/hotel.html',context=context)


# 酒店
def hotel(request):
    myspace = 0
    attraction_user = 0
    hotel_user = 0
    if request.session.get('username'):
        login = request.session.get('username')
        user = AuthUser.objects.get(username=login)
        if user.attractions_user == 0 and user.hotel_user == 0:
            myspace = 1
        if user.attractions_user != 0 and user.hotel_user == 0:
            attraction_user = 1
        if user.attractions_user == 0 and user.hotel_user != 0:
            hotel_user = 1
    else:
        login = None

    # 携带数据传输
    context = {
        'hotel_datail': HotelDatail.objects.all(),
        'username': login,
        'myspace': myspace,
        'attraction_user': attraction_user,
        'hotel_user': hotel_user,
    }
    return render(request, 'templates/attractions.html',context=context)


# 新闻
def news(request):
    if request.session.get('username'):
        login=request.session.get('username')
    else:
        login=None
    context={
        'username': login
    }
    return render(request,'templates/news.html',context=context)


# 景区流量
def flow(request):
    if request.session.get('username'):
        login=request.session.get('username')
    else:
        login=None
    context={
        'username': login
    }
    return render(request,'templates/flow.html',context=context)


# 登录
def login(request):
    return render(request, 'login-page.html')


def login_inspect(request):
    global password, username, yzm
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        yzm = request.POST['yzm']

    # 验证码认证
    if yzm.upper()!=out_string.upper():
        context={
            'yzm':0
        }
        return render(request,'login-page.html',context=context)

    # 登录验证
    try:
        user=AuthUser.objects.get(username=username)
        encode=user.password
        if check_password(password,encode):
            request.session['username']=username
            refresh=AuthUser.objects.get(username=username)
            refresh.last_login=timezone.now()
            refresh.save()
            request.session['username']=username
            return redirect(reverse('home:home'))
        else:
            context={
                'password':0,
            }
            return render(request,'login-page.html',context=context)
    except BaseException:
        context={
            'username':0,
        }
        return render(request,'login-page.html',context=context)


# 个人中心
def my_space(request):
    if request.session.get('username'):
        user=request.session.get('username')
        user_id=AuthUser.objects.get(username=user).user_id
        information=UserInformation.objects.get(id=user_id)
        context={
            "username":user,
            "information":information,
        }
        return render(request, 'templates/my_backstage/about_me.html', context=context)
    else:
        return redirect(reverse("home:login"))

def my_order(request):
    if request.session.get('username'):
        user_id=AuthUser.objects.get(username=request.session.get('username')).id
        order=UserOrder.objects.filter(user_id=user_id)
        attraction=[]
        hotel=[]
        attraction_datail = []
        hotel_datail = []
        for i in order:
            if i.attraction_order==None:
                hotel.append(i.hotel_order)
            else:
                attraction.append(i.attraction_order)
        print(hotel)
        print(attraction)
        for i in range(len(attraction)):
            attraction_datail.append(AttractionsOrder.objects.get(id=attraction[i]))
        for i in range(len(hotel)):
            hotel_datail.append(HotelOrder.objects.get(id=hotel[i]))
        '''
        for i in range(len(attraction)):
            orders=AttractionsOrder.objects.get(id=attraction[i])
            attraction_id=orders.attractions_id
            attractions=AttractionsDatail.objects.get(id=attraction_id)
            name=attractions.name
            attraction_datail.setdefault('orderid',[]).append(attraction[i])
            attraction_datail.setdefault('name',[]).append(name)
            attraction_datail.setdefault('username',[]).append(request.session.get('username'))
            attraction_datail.setdefault('price',[]).append(orders.price)
            attraction_datail.setdefault('auth_time',[]).append(orders.auth_time)
            attraction_datail.setdefault('use_time',[]).append(orders.use_time)
            attraction_datail.setdefault('phone',[]).append(orders.phone)
            attraction_datail.setdefault('usename',[]).append(orders.name)
        for i in range(len(hotel)):
            orders=HotelOrder.objects.get(id=hotel[i])
            hotel_id=orders.hotel_id
            home_id=orders.home_id
            hotel_name=HotelDatail.objects.get(id=hotel_id).name
            home_name=HomeDatail.objects.get(id=home_id,hotel_id=hotel_id).home
            hotel_datail.setdefault('orderid',[]).append(hotel[i])
            hotel_datail.setdefault('hotel_name',[]).append(hotel_name)
            hotel_datail.setdefault('home_name',[]).append(home_name)
            hotel_datail.setdefault('name',[]).append(orders.name)
            hotel_datail.setdefault('phone',[]).append(orders.phone)
            hotel_datail.setdefault('id_card',[]).append(orders.id_card)
            hotel_datail.setdefault('person',[]).append(orders.person)
            hotel_datail.setdefault('data',[]).append(orders.data)
            hotel_datail.setdefault('come_time',[]).append(orders.come_time)
            hotel_datail.setdefault('live_time',[]).append(orders.live_time)
            hotel_datail.setdefault('price',[]).append(orders.price)
            hotel_datail.setdefault('auth_time',[]).append(orders.auth_time)
        '''
        context={
            'hotel_order':hotel_datail,
            'attraction_order':attraction_datail,
            'attraction':AttractionsDatail.objects.all(),
            'hotel':HotelDatail.objects.all(),
            'home':HomeDatail.objects.all(),
        }
        return render(request, 'templates/my_backstage/order.html',context=context)
    else:
        return redirect(reverse("home:login"))

def change_password(request):
    if request.session.get('username'):
        user=AuthUser.objects.get(username=request.session.get('username'))
        passowrd=user.password
        context={
            "password":passowrd,
        }
        return render(request, 'templates/my_backstage/change_password.html',context=context)
    else:
        return redirect(reverse("home:login"))

def change_information(request):
    if not request.session.get('username'):
        return redirect(reverse("home:login"))

    if request.POST:
        username=request.POST['username']
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        qq=request.POST['QQ']
        address=request.POST['address']

        user=request.session.get('username')
        users=AuthUser.objects.get(username=user)
        users.username=username
        users.save()
        information=UserInformation.objects.get(id=users.user_id)
        information.name=name
        information.phone=phone
        information.email=email
        information.qq=qq
        information.address=address
        information.save()

        return redirect(reverse("home:home"))

def change(request):
    if not request.session.get('username'):
        return redirect(reverse("home:login"))
    if request.POST:
        password=request.POST['password']
        new_password=request.POST['new_password']
        email=request.POST['email']

        user=request.session.get('username')
        encode=AuthUser.objects.get(username=user).password
        if check_password(password=password,encoded=encode):
            password=make_password(password=new_password)
            users=AuthUser.objects.get(username=user)
            users.password=password
            users.save()
            return redirect(reverse("home:sign_out"))
        else:
            return redirect(reverse("home:change_password"))


# 注册
def regist(request):
    return render(request, 'regist-page.html')


def hotel_regist(request):
    return render(request, 'hotel_regist.html')


def attractions_regist(request):
    return render(request, 'attractions_regist.html')


def regist_inspect(request):
    global email, phone, yzm, username, password
    now_time=timezone.now()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        yzm = request.POST['yzm']
    password=make_password(password)
    for user in AuthUser.objects.all():
        if user.username == username:
            context = {
                'username': 0,
            }
            return render(request, 'regist-page.html', context=context)
    if yzm.upper() != out_string.upper():
        context = {
            'yzm': 0,
        }
        return render(request, 'regist-page.html', context=context)
    user_information=UserInformation(phone=phone,email=email)
    user_information.save()
    auth_user=AuthUser(username=username,password=password,user_id=user_information.id,is_superuser=0,is_staff=0,last_login=timezone.now(),date_joined=timezone.now(),hotel_user=0,attractions_user=0)
    auth_user.save()
    return redirect(reverse('home:login'))


def attractions_inspect(request):
    global attractions_name, phone, email, yzm, password, username
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        attractions_name=request.POST['attractions_name']
        email=request.POST['email']
        phone=request.POST['phone']
        yzm=request.POST['yzm']
    password=make_password(password)
    for user in AuthUser.objects.all():
        if user.username == username:
            print(username)
            context = {
                'username': 0,
            }
            return render(request, 'regist-page.html', context=context)
    if yzm.upper() != out_string.upper():
        context = {
            'yzm': 0,
        }
        return render(request, 'regist-page.html', context=context)
    user_information = UserInformation(phone=phone, email=email)
    user_information.save()
    user_id=user_information.id
    attraction=AttractionsDatail(name=attractions_name,phone=phone,email=email)
    attraction.save()
    attraction_id=attraction.id
    auth_user = AuthUser(username=username,password=password, user_id=user_id, is_superuser=0,
                         is_staff=0,hotel_user=0, attractions_user=attraction_id, last_login=timezone.now(),
                         date_joined=timezone.now())
    auth_user.save()
    return redirect(reverse('home:login'))


def hotel_inspect(request):
    global hotel_name, phone, email, yzm, username, password
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        hotel_name = request.POST['hotel_name']
        email = request.POST['email']
        phone = request.POST['phone']
        yzm = request.POST['yzm']
    password=make_password(password)
    for user in AuthUser.objects.all():
        if user.username == username:
            print(username)
            context = {
                'username': 0,
            }
            return render(request, 'regist-page.html', context=context)
    if yzm.upper() != out_string.upper():
        context = {
            'yzm': 0,
        }
        return render(request, 'regist-page.html', context=context)
    user_information = UserInformation(phone=phone, email=email)
    user_information.save()
    user_id=user_information.id
    hotels=HotelDatail(name=hotel_name,phone=phone,email=email)
    hotels.save()
    hotel_id=hotels.id
    auth_user = AuthUser(username=username,password=password, user_id=user_id, is_superuser=0,
                         is_staff=0, hotel_user=hotel_id,attractions_user=0, last_login=timezone.now(),
                         date_joined=timezone.now())
    auth_user.save()

    return redirect(reverse('home:login'))

# 详细信息渲染
def attractions_datail(request,datail):
    attraction_datail = AttractionsDatail.objects.get(name=datail)
    try:
        flow = Flow.objects.get(name_id=attraction_datail.id)
    except:
        flow = {
            'time1_flow': '',
            'time2_flow': '',
            'time3_flow': '',
            'time4_flow': '',
            'time5_flow': '',
            'time6_flow': '',
        }
    price = AttractionsPrice.objects.filter(name_id=attraction_datail.id)
    attraction_img = AttractionsImg.objects.filter(attractions_id=attraction_datail.id)
    if len(attraction_img)==0:
        attraction_img=''
    try:
        public = PublicityPhoto.objects.get(attractions_id=attraction_datail.id)
    except:
        public=''


    context={
        'attractions':1,
        'attraction_datail':attraction_datail,
        'attraction_img':attraction_img,
        'flow':flow,
        'price':price,
        'public':public,
    }
    return render(request,'templates/datail.html',context=context)


def hotel_datail(request,datail):
    hotel=HotelDatail.objects.get(name=datail)
    home=HomeDatail.objects.filter(hotel_id=hotel.id)
    hotel_img=HotelImg.objects.filter(hotel_id=hotel.id)
    if len(hotel_img)==0:
        hotel_img=''
    context={
        'hotels':1,
        'hotel':hotel,
        'home':home,
        'hotel_img':hotel_img,

    }
    return render(request,'templates/datail.html',context=context)


#登出
def sign_out(request):
    request.session.flush()
    return redirect(reverse('home:home'))

# 定义全局变量，进行验证码认证
out_string = ''


# 验证码
def verification(request):
    global out_string, fill_point, fill_line
    out_string = ''
    string_small = 'qwertyuiopasdfghjklzxcvbnm'
    string_big = string_small.upper()
    num = '0123456789'
    string = string_big + string_small + num
    mode = 'RGB'
    size = (100, 46)
    color = (248, 248, 255)
    image = Image.new(mode=mode, size=size, color=color)
    draw = ImageDraw.Draw(image, mode=mode)
    imagefont = ImageFont.truetype('/static/Font/Sitka.ttc', 30)
    # fill=(255,0,0)
    # draw.text(xy=(0,0),text='ad',font=imagefont,fill=fill)
    # 绘制干扰线
    for i in range(0, 15):
        begin = (random.randint(0, size[0]), random.randint(0, size[1]))
        end = (random.randint(0, size[0]), random.randint(0, size[1]))
        fill_line = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.line([begin, end], fill=fill_line)

    # 绘制干扰点
    for i in range(0, size[0]):
        for j in range(0, 10):
            fill_point = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.point((random.randint(0, size[0]), random.randint(0, size[1])), fill=fill_point)

    # 绘制随机字符
    for i in range(0, 6):
        num = random.randint(0, len(string) - 1)
        fill_font = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if fill_line == fill_font or fill_point == fill_font:
            fill_font = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.text(xy=(random.uniform(16 * i, 15 * (i + 1)), 10), text=string[num], font=imagefont, fill=fill_font)
        out_string = out_string + string[num]

    fp = BytesIO()
    image.save(fp, 'png')
    print(out_string)
    return HttpResponse(fp.getvalue(), content_type='image/png')