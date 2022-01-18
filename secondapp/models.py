from django.db import models
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()
# Create your models here.
class Armyshop(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    type = models.TextField()
    name = models.TextField()
    class Meta:
        db_table = 'army_shop'
        managed = False