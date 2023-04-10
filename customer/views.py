from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Admin.models import ureg,login,Account
from shop.models import vegdet,stocks
from.models import cart,order_master,order_child
import datetime
# Create your views here.
def userhome(request):
    context = {}
    template = loader.get_template("userhome.html")
    return HttpResponse(template.render(context, request))
def ureg1(request):
    if request.method=="POST":
        name=request.POST.get("name")
        hname=request.POST.get("hname")
        loc=request.POST.get("loc")
        pin=request.POST.get("pin")
        lmark=request.POST.get("lmark")
        phone=request.POST.get("phone")
        uname=request.POST.get("uname")
        pwd=request.POST.get("password")
        s=ureg()
        s.name=name
        s.hname=hname
        s.location=loc
        s.pin=pin
        s.lmark=lmark
        s.phone=phone
        s.uname=uname
        s.pwd=pwd
        s.status='pending'
        s.save()
        l=login()
        l.uname=uname
        l.pwd=pwd
        l.utype='user'
        l.save()
        return HttpResponse("<script>alert('Register successfully');window.location='/ureg';</script>")

    else:
        context = {}
        template = loader.get_template("userreg.html")
        return HttpResponse(template.render(context, request))
def searchitems(request):
    v=vegdet.objects.raw("select shop_vegdet.id,shop_vegdet.vegname,shop_vegdet.rate,shop_vegdet.image,shop_stocks.st,admin_category.cname from shop_vegdet,shop_stocks,admin_category where admin_category.id=shop_vegdet.category and shop_vegdet.id=shop_stocks.vid and shop_vegdet.status='approve'")
    context = {'key':v}
    template = loader.get_template("searchitems.html")
    return HttpResponse(template.render(context, request))
def searchitems1(request,id):
    request.session["vid"]=id
    v = vegdet.objects.raw("select shop_vegdet.id,shop_vegdet.vegname,shop_vegdet.rate,shop_vegdet.image,shop_stocks.st,admin_category.cname from shop_vegdet,shop_stocks,admin_category where admin_category.id=shop_vegdet.category and shop_vegdet.id=shop_stocks.vid and shop_vegdet.status='approve' and shop_vegdet.id=%s",[id])
    context = {'key': v}
    template = loader.get_template("searchitems1.html")
    return HttpResponse(template.render(context, request))
def addcart(request):
    c=cart()
    c.vid=request.session["vid"]
    uname=request.session["uname"]
    uid=ureg.objects.get(uname=uname)
    c.uid=uid.id
    c.qty=request.POST.get("qty")
    c.bdate=request.POST.get("bdate")
    vid=request.session["vid"]
    qty=request.POST.get("qty")
    v=vegdet.objects.get(id=vid)
    rate=v.rate
    tot=int(qty)*int(rate)
    c.total=tot
    c.save()
    return HttpResponse("<script>alert('Item Selected successfully');window.location='/searchitems';</script>")
def viewcart(request):
    uname=request.session["uname"]
    uid=ureg.objects.get(uname=uname)
    c=cart.objects.raw("select customer_cart.*,admin_category.cname,shop_vegdet.vegname,shop_vegdet.rate from customer_cart,admin_category,admin_ureg,shop_vegdet where admin_ureg.id=customer_cart.uid and customer_cart.vid=shop_vegdet.id and shop_vegdet.category=admin_category.id and admin_ureg.id=%s",[uid.id])
    t=cart.objects.raw("select sum(customer_cart.total) as tot,customer_cart.id from customer_cart")

    context = {'key': c,'t':t}
    template = loader.get_template("viewcart.html")
    return HttpResponse(template.render(context, request))
def deletecart(request,id):
    c=cart.objects.get(id=id)
    c.delete()
    return HttpResponse("<script>alert('Item deleted');window.location='/viewcart';</script>")

def phome(request):
    template = loader.get_template("paymenthome.html")
    context = {}
    return HttpResponse(template.render(context, request))
def paymentcon(request):

     cno = request.POST.get("cno")
     request.session["cno"] = cno
     sum = request.session["amount"]
     if (Account.objects.get(cno=cno)):
        x = Account.objects.get(cno=cno)
        context = {'sum': sum, 'card': x}
        template = loader.get_template("paymentcon.html")
        return HttpResponse(template.render(context, request))
     else:
        return HttpResponse("<script>alert('invalid card no');window.location='/payment';</script>")
def payment(request):
    request.session["amount"]=request.POST.get("total")

    context = {}
    template = loader.get_template("payment.html")
    return HttpResponse(template.render(context, request))
def savepayment(request):
    uname=request.session["uname"]
    uid=ureg.objects.get(uname=uname)
    c=cart.objects.filter(uid=uid.id)
    o=order_master()
    o.uid=uid.id
    o.gtotal=request.session["amount"]
    o.odate=datetime.datetime.now()
    o.status='pending'
    o.save()
    oid=order_master.objects.raw("select max(customer_order_master.id) as id from customer_order_master")
    for i in oid:
        oid1=i.id
    for i in c:
        o1=order_child()
        o1.oid=oid1
        c1=cart.objects.get(id=i.id)
        o1.vid=c1.vid
        o1.qty=c1.qty
        o1.total=c1.total
        o1.status='pending'
        o1.save()
        s=stocks.objects.get(vid=c1.vid)
        st=int(s.st)
        q=c1.qty
        nst=st-int(q)
        s.st=nst
        s.save()
    c.delete()
    return HttpResponse("<script>alert('payment completed successfully');window.location='/uhome';</script>")
def uservieworderstatus(request):
    uname=request.session["uname"]
    oid=ureg.objects.get(uname=uname)
    o=order_master.objects.raw("select distinct(admin_ureg.name),admin_ureg.location,admin_ureg.lmark,admin_ureg.phone,customer_order_master.* from admin_ureg,customer_order_master,customer_order_child,shop_vegdet,admin_oreg where admin_ureg.id=customer_order_master.uid and customer_order_master.id=customer_order_child.oid and customer_order_child.vid=shop_vegdet.id and admin_ureg.id=%s",[oid.id])
    context = {'key': o}
    template = loader.get_template("uservieworderstatus.html")
    return HttpResponse(template.render(context, request))
def uservieworderstatus1(request,id):
    uname=request.session["uname"]
    request.session["orderid"]=id
    oid=ureg.objects.get(uname=uname)

    o=order_child.objects.raw("select customer_order_child.*,admin_category.cname,shop_vegdet.vegname,shop_vegdet.rate from customer_order_master,customer_order_child,shop_vegdet,admin_category where customer_order_master.id=customer_order_child.oid and customer_order_child.vid=shop_vegdet.id and shop_vegdet.category=admin_category.id and customer_order_master.id=%s",[id])
    context = {'key': o}
    template = loader.get_template("uservieworderstatus1.html")
    return HttpResponse(template.render(context, request))
def cancelorder(request):
    uname=request.session["uname"]
    oid=ureg.objects.get(uname=uname)
    o=order_master.objects.raw("select distinct(admin_ureg.name),admin_ureg.location,admin_ureg.lmark,admin_ureg.phone,customer_order_master.id,customer_order_master.* from admin_ureg,customer_order_master,customer_order_child,shop_vegdet,admin_oreg where admin_ureg.id=customer_order_master.uid and customer_order_master.id=customer_order_child.oid and customer_order_child.vid=shop_vegdet.id and customer_order_master.status='pending' and  admin_ureg.id=%s",[oid.id])
    context = {'key': o}
    template = loader.get_template("cancelorder.html")
    return HttpResponse(template.render(context, request))
def cancelorder1(request,id):
    uname=request.session["uname"]
    request.session["orderid"]=id
    oid=ureg.objects.get(uname=uname)

    o=order_child.objects.raw("select customer_order_child.*,admin_category.cname,shop_vegdet.vegname,shop_vegdet.rate from customer_order_master,customer_order_child,shop_vegdet,admin_category where customer_order_master.id=customer_order_child.oid and customer_order_child.vid=shop_vegdet.id and shop_vegdet.category=admin_category.id and customer_order_master.id=%s",[id])
    context = {'key': o}
    template = loader.get_template("cancelorder1.html")
    return HttpResponse(template.render(context, request))
def cancelorder2(request):
    oid=request.session["orderid"]
    c=order_master.objects.get(id=oid)
    c.status='cancel'
    c.save()
    return HttpResponse("<script>alert('ordercanceled successfully');window.location='/cancelorder';</script>")

