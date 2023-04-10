from django.db import models

# Create your models here.
class vegdet(models.Model):
    vegname=models.CharField(max_length=20)
    category=models.IntegerField()
    rate=models.IntegerField()
    image=models.FileField(upload_to='file')
    des=models.CharField(max_length=50)
    stock=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='')
    oid=models.IntegerField(default=0)
class stocks(models.Model):
    vid=models.IntegerField()
    st=models.IntegerField()
class assign(models.Model):
    orderid=models.IntegerField()
    sid=models.IntegerField()
    oid=models.IntegerField(default=1)
    status=models.CharField(max_length=10)

