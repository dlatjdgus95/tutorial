from django.db import models
from django.db.models.fields import CharField, IntegerField
class Shop(models.Model):
    shop_id = IntegerField(primary_key=True)
    shop_name = CharField(max_length=100, null=True)
    shop_desc = CharField(max_length=100, null=True)
    rest_date = CharField(max_length=100, null=True)
    parking_info = CharField(max_length=100, null=True)
    img_path = CharField(max_length=255, null=True)
    class Meta:
        db_table = 'shop'
        app_label = 'thirdapp'
        managed = False
# Create your models here.
class Jeju(models.Model):
    id = IntegerField(primary_key=True)
    course = CharField(max_length=10,null=True)
    course_name = CharField(max_length=20,null=True)
    distance = models.FloatField(null=True)
    time_info = CharField(max_length=10,null=True)
    start_end_info = CharField(max_length=30,null=True)
    cre_date = models.DateField(auto_now=False, auto_now_add=False)
    class Meta:
        db_table = 'jeju_olle'
        app_label = 'thirdapp'
        managed = False
