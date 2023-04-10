from django.db import models

# Create your models here.
class cart(models.Model):
    bdate=models.DateField()
    uid=models.IntegerField()
    vid=models.IntegerField()
    qty=models.IntegerField()
    total=models.IntegerField()
class order_master(models.Model):
    odate = models.DateField()

    uid=models.IntegerField()
    status=models.CharField(max_length=10)
    gtotal=models.IntegerField()
class order_child(models.Model):
    oid=models.IntegerField()
    vid=models.IntegerField()
    qty=models.IntegerField()
    total=models.IntegerField()
    status=models.CharField(max_length=20)