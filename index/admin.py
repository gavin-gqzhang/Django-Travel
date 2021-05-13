from django.contrib import admin

from .models import AttractionsDatail,AttractionsPrice,Flow,HomeDatail,HotelDatail,News,HotelOrder,AttractionsOrder
#数据库后台
# # 后台一对多编辑
# class hotel_editor(admin.StackedInline):
#     model = HomeDatail
#     extra = 2
#
# class attraction_editor(admin.StackedInline):
#     model = AttractionsPrice,Flow
#     extra = 2
#
# # 后台显示属性
# class HotelDatail_display(admin.ModelAdmin):
#     list_display = ['name','max_price','min_price','max_price','address','phone']
#     inlines = [hotel_editor,]
#
# class Attractions_display(admin.ModelAdmin):
#     list_display = ['name','city','area','type','suggest']
#     inlines = [attraction_editor,]
#
# class BannerImg_display(admin.ModelAdmin):
#     list_display = ['img','href']
#
#
#
# # Register your models here.
# admin.site.register(HotelDatail,HotelDatail_display)
# # admin.site.register(HomeDatail)
# # admin.site.register(HotelOrder)
# # admin.site.register(AttractionsOrder)
# admin.site.register(AttractionsDatail,Attractions_display)
# # admin.site.register(AttractionsPrice)
# # admin.site.register(Flow)
# admin.site.register(News)
#
#
# 创建窗口下方删除功能
action_on_bottom=True

# 取消窗口上方删除功能
action_on_top=False

# 后台搜索栏
search_fields=['name']



