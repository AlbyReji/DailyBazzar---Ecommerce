from django.db import models

# Create your models here.

class category(models.Model):
    cname=models.CharField(max_length=20)
class login(models.Model):
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    utype=models.CharField(max_length=10)

class Bank(models.Model):
    bname=models.CharField(max_length=50)
    logo=models.ImageField(upload_to="logo")
class Branch(models.Model):
    branch=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    ifsc=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    bname=models.IntegerField()
class Account(models.Model):
    cname=models.CharField(max_length=50)
    cno=models.BigIntegerField()
    cvv=models.IntegerField()
    year=models.IntegerField()
    month=models.IntegerField()
    amount=models.BigIntegerField()
    bname=models.IntegerField()
    branch=models.IntegerField()
class ureg(models.Model):
    name=models.CharField(max_length=20)
    hname=models.CharField(max_length=50)
    location=models.CharField(max_length=20)
    pin=models.IntegerField()
    lmark=models.CharField(max_length=20)
    phone=models.IntegerField()
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    status = models.CharField(max_length=20,default='')
class oreg(models.Model):
    name = models.CharField(max_length=20)
    shname = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    rno = models.IntegerField()
    lmark = models.CharField(max_length=20)
    cno = models.IntegerField()
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='')
class staff(models.Model):
    sname=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    oid=models.IntegerField(default=0)
