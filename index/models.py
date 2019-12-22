from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils import timezone

class AttractionsDatail(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    datail = models.TextField(blank=True, null=True)
    suggest = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    max_num = models.IntegerField(blank=True, null=True)
    max_price = models.FloatField(blank=True, null=True)
    min_price = models.FloatField(blank=True, null=True)
    in_time = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attractions_datail'


class AttractionsImg(models.Model):
    attractions_id = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attractions_img'


class AttractionsOrder(models.Model):
    attractions_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    auth_time = models.DateTimeField(blank=True, null=True)
    use_time = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    price_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attractions_order'


class AttractionsPrice(models.Model):
    name_id = models.IntegerField(blank=True, null=True)
    ticket_name = models.CharField(max_length=255, blank=True, null=True)
    ticket_price = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attractions_price'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    hotel_user = models.IntegerField(blank=True, null=True)
    attractions_user = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Flow(models.Model):
    name_id = models.IntegerField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    time1_flow = models.FloatField(blank=True, null=True)
    time2_flow = models.FloatField(blank=True, null=True)
    time3_flow = models.FloatField(blank=True, null=True)
    time4_flow = models.FloatField(blank=True, null=True)
    time5_flow = models.FloatField(blank=True, null=True)
    time6_flow = models.FloatField(blank=True, null=True)
    flow_img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow'


class HomeDatail(models.Model):
    hotel_id = models.IntegerField(blank=True, null=True)
    home = models.CharField(max_length=255, blank=True, null=True)
    person_num = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    datail = models.TextField(blank=True, null=True)
    clean = models.IntegerField(blank=True, null=True)
    get_person = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_datail'


class HotelDatail(models.Model):
    manager = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    max_price = models.FloatField(blank=True, null=True)
    min_price = models.FloatField(blank=True, null=True)
    datail = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    sum_order = models.IntegerField(blank=True, null=True)
    home_num = models.IntegerField(blank=True, null=True)
    in_time = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_datail'


class HotelImg(models.Model):
    home_id = models.IntegerField(blank=True, null=True)
    hotel_id = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_img'


class HotelOrder(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    hotel_id = models.IntegerField(blank=True, null=True)
    home_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    id_card = models.CharField(max_length=255, blank=True, null=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    data = models.CharField(max_length=255, blank=True, null=True)
    come_time = models.CharField(max_length=255, blank=True, null=True)
    live_time = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    auth_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_order'


class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    news_img = models.CharField(max_length=255, blank=True, null=True)
    auth_time = models.TimeField(blank=True, null=True)
    datail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class PublicityPhoto(models.Model):
    hotel_id = models.IntegerField(blank=True, null=True)
    attractions_id = models.IntegerField(blank=True, null=True)
    upload = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicity_photo'


class UserInformation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    qq = models.CharField(max_length=255, blank=True, null=True)
    datail = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_information'


class UserOrder(models.Model):
    hotel_order = models.IntegerField(blank=True, null=True)
    attraction_order = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_order'
