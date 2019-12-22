from django.shortcuts import render, redirect
from django.urls import reverse
from index.models import *
import calendar
from datetime import datetime
import re
'''
    发送邮件
'''
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
# Create your views here.

'''
    时间判断
'''
def get_time():
    time=timezone.localdate()
    year = time.strftime('%Y')
    mouth=time.strftime('%m')
    day=time.strftime('%d')
    times=[]
    times.append(datetime(year=int(year),month=int(mouth),day=int(day)).strftime('%Y-%m-%d'))
    for i in range(1,8):
        if int(day)+1>int(calendar.monthrange(int(year),int(mouth))[1]) and mouth+1!=13:
            day=1
            mouth=int(mouth)+1
            now=datetime(year=int(year),month=mouth,day=day)
        elif int(day)+1>int(calendar.monthrange(int(year),int(mouth))[1]) and mouth+1==13:
            day=1
            mouth=1
            year=int(year)+1
            now=datetime(year=year,month=mouth,day=day)
        else:
            day=int(day)+1
            now=datetime(year=int(year),month=int(mouth),day=int(day))
        now = now.strftime('%Y-%m-%d')
        times.append(now)

    return times

'''
    时间判断
'''
def get_minute():
    time=timezone.localtime()
    hour=time.strftime('%H')
    minute=time.strftime('%M')
    times=[]
    for i in range(48):
        if i==0:
            if int(minute)<=30:
                now=("{}:{} - {}:{}".format(int(hour),30,int(hour)+1,'00'))
            else:
                now=("{}:{} - {}:{}".format(int(hour)+1,'00',int(hour)+1,30))
            hour=int(hour)+1
        if int(hour)==24 and i!=0:
            break
        if int(hour)!=24 and i!=0:
            now = ("{}:{} - {}:{}".format((hour - 1), 30, hour, '00'))
            times.append(now)
            if int(minute)<=30:
                now=("{}:{} - {}:{}".format(int(hour),30,int(hour)+1,'00'))
            else:
                now=("{}:{} - {}:{}".format(int(hour),'00',int(hour),30))
            # times.append(now)
        hour=int(hour)+1
        times.append(now)

    return times


'''
    预订酒店房间页面
'''
def place_order(request,hotel,home):
    if request.session.get('username'):
        hotel_id=HotelDatail.objects.get(name=hotel)
        homes=HomeDatail.objects.filter(hotel_id=hotel_id.id)
        for i in homes:
            if i.home == home:
                price=i.price
                num=i.num
                datail=i.datail
                break
        context={
            'username':request.session.get('username'),
            'price':price,
            'num':num,
            'datail':datail,
            'hotel':hotel,
            'home':home,
            'get_time':get_time(),
            'get_minute':get_minute(),
        }
        return render(request, 'order/hotel.html',context=context)
    else:
        return redirect(reverse("home:login"))

'''
    提交预订
'''
def home_order(request):
    if not request.session.get('username'):
        return redirect(reverse("home:login"))
    if request.POST:
        hotel=request.POST['hotel']
        home=request.POST['home']
        name=request.POST['name']
        id_card=request.POST['card']
        person=request.POST['person']
        data=request.POST['data']
        phone=request.POST['phone']
        live=request.POST['live_time']
        come_time=request.POST['come_time']
        price=request.POST['price']
    username=request.session.get('username')
    user=AuthUser.objects.get(username=username)
    user_id=user.id
    hotel_id=HotelDatail.objects.get(name=hotel).id
    homes=HomeDatail.objects.get(home=home,hotel_id=hotel_id)
    home_id=homes.id
    home_price=homes.price
    order=HotelOrder(
        user_id=user_id,
        hotel_id=hotel_id,
        home_id=home_id,
        name=name,
        phone=phone,
        id_card=id_card,
        person=person,
        data=data,
        live_time=live,
        come_time=come_time,
        price=float(home_price)*int(data),
        auth_time=timezone.now(),
    )
    order.save()
    homes.num=homes.num-int(data)
    homes.save()
    user_order=UserOrder(
        hotel_order=order.id,
        user_id=user_id
    )
    user_order.save()
    mail(name=name,auth_time=timezone.now(),use_time=live,use_name=hotel,num=data,price=float(home_price)*int(data))
    return redirect(reverse('home:my_order'))

'''
    景区门票预订
'''
def attraction_order(request,attraction):
    if not request.session.get('username'):
        return redirect(reverse('home:login'))
    attraction_datail=AttractionsDatail.objects.get(name=attraction)
    in_time=attraction_datail.in_time
    attraction_id=attraction_datail.id
    price=[]
    attraction_price=AttractionsPrice.objects.filter(name_id=attraction_id)
    for i in attraction_price:
        prices=('{}  {}元'.format(i.ticket_name,i.ticket_price))
        price.append(prices)

    context={
        'attraction':attraction,
        'price':price,
        'in_time':in_time,
        'user_time':get_time(),
    }
    return render(request, 'order/attraction.html',context=context)


'''
    门票预订提交
'''
def get_attraction(request):
    if not request.session.get('username'):
        return redirect(reverse('home:login'))
    if request.POST:
        phone=request.POST['phone']
        name=request.POST['name']
        price=request.POST['price']
        use_time=request.POST['user_time']
        num=request.POST['num']
        attraction=request.POST['attraction']
    attractions=AttractionsDatail.objects.get(name=attraction)
    attraction_id=attractions.id
    user=request.session.get('username')
    users=AuthUser.objects.get(username=user)
    user_id=users.id
    price=re.findall('\d*.\d*元',price)[0]
    price=(price[:-1])
    attraction_price=AttractionsPrice.objects.get(name_id=attraction_id,ticket_price=price)
    attraction_price.num=int(attraction_price.num)+int(num)
    attraction_price.save()
    order=AttractionsOrder(
        attractions_id=attraction_id,
        user_id=user_id,
        price=float(price)*int(num),
        phone=phone,
        name=name,
        use_time=use_time,
        auth_time=timezone.now(),
        num=num,
        price_id=attraction_price.id,
    )
    order.save()
    user_order=UserOrder(
        user_id=user_id,
        attraction_order=order.id,
    )
    user_order.save()
    mail(name=name,auth_time=timezone.now(),use_time=use_time,use_name=attraction,num=num,price=float(price)*int(num))
    return redirect(reverse('home:my_order'))

def mail(name,auth_time,use_time,use_name,num,price):
    host_server='smtp.qq.com'
    sender_qq='2230685848'
    pwd='gzxaermzydgdecbj'
    send_mail = '2230685848@qq.com'
    receivers = '2230685848@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    mail_content="""
    <p>预订订单成功</p>
    <table border="1">
        <tr>
            <td style="width:100px;height:100px">使用人</td>
            <td style="width:100px;height:100px">下单时间</td>
            <td style="width:100px;height:100px">使用时间</td>
            <td style="width:100px;height:100px">订单使用单位</td>
            <td style="width:100px;height:100px">数量</td>
            <td style="width:100px;height:100px">价格</td>
        </tr>
        <tr>
            <td style="width:100px;height:100px">{0}</td>
            <td style="width:100px;height:100px">{1}</td>
            <td style="width:100px;height:100px">{2}</td>
            <td style="width:100px;height:100px">{3}</td>
            <td style="width:100px;height:100px">{4}</td>
            <td style="width:100px;height:100px">{5}</td>
        </tr>
    </table>
    """.format(name,auth_time,use_time,use_name,num,price)
    mail_title='预订成功'

    smtp=SMTP_SSL(host_server)
    smtp.ehlo(host_server)
    smtp.login(sender_qq,pwd)

    msg=MIMEText(mail_content, 'html','utf-8')
    msg['Subject']=Header(mail_title,'utf-8')
    msg['From']=send_mail
    msg['To']=receivers
    smtp.sendmail(send_mail,receivers,msg.as_string())
    smtp.quit()