from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import oreg,category,staff,ureg,login,Bank,Branch,Account
from customer.models import order_child
from shop.models import vegdet
from django.http import JsonResponse
# Create your views here.

def login1(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("password")
        if(login.objects.filter(uname=uname,pwd=pwd)):
            l=login.objects.filter(uname=uname,pwd=pwd)
            for i in l:
                utype=i.utype
            if(utype=="admin"):
                context = {}
                template = loader.get_template("admin.html")
                return HttpResponse(template.render(context, request))
            elif(utype=="owner"):
                o=oreg.objects.filter(uname=uname)
                for i in o:
                    status=i.status
                if(status=="pending"):
                    return HttpResponse("<script>alert('Access Denied');window.location='/login';</script>")
                else:
                    request.session["uname"]=uname
                    context = {}
                    template = loader.get_template("ownerhome.html")
                    return HttpResponse(template.render(context, request))
            elif (utype == "user"):
                o = ureg.objects.filter(uname=uname)
                for i in o:
                    status = i.status
                if (status == "pending"):
                    return HttpResponse("<script>alert('Access Denied');window.location='/login';</script>")
                else:
                    request.session["uname"]=uname
                    context = {}
                    template = loader.get_template("userhome.html")
                    return HttpResponse(template.render(context, request))
            elif(utype=="staff"):
                request.session["uname"] = uname
                context = {}
                template = loader.get_template("staffhome.html")
                return HttpResponse(template.render(context, request))




        else:
            return HttpResponse("<script>alert('invalid username or password');window.location='/login';</script>")


    else:
        context = {}
        template = loader.get_template("login.html")
        return HttpResponse(template.render(context, request))
def index(request):
    context = {}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))
def admin1(request):
    context = {}
    template = loader.get_template("admin.html")
    return HttpResponse(template.render(context, request))


def category1(request):
    if request.method=="POST":
        cname=request.POST.get("cname")
        s=category()
        s.cname=cname
        s.save()
        return HttpResponse("<script>alert('Category Added successfully');window.location='/category';</script>")

    else:
        context = {}
        template = loader.get_template("addcategory.html")
        return HttpResponse(template.render(context, request))
def staff1(request):
    if request.method=="POST":
        sname=request.POST.get("sname")
        gender=request.POST.get("gender")
        designation=request.POST.get("designation")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        uname=request.POST.get("uname")
        pwd=request.POST.get("pwd")
        s=staff()
        s.sname=sname
        s.gender=gender
        s.designation=designation
        s.email=email
        s.phone=phone
        s.uname=uname
        s.pwd=pwd
        uname1=request.session["uname"]
        oid=oreg.objects.get(uname=uname1)
        s.oid= oid.id
        l=login()
        l.uname=uname
        l.pwd=pwd
        l.utype='staff'
        l.save()
        s.save()
        return HttpResponse("<script>alert('Deliverer Added successfully');window.location='/ohome';</script>")
    else:
        context = {}
        template = loader.get_template("addstaffdetails.html")
        return HttpResponse(template.render(context, request))

def approveusers(request):
    s=ureg.objects.filter(status='pending')
    context={'key':s}
    template = loader.get_template("approveusers.html")
    return HttpResponse(template.render(context, request))
def approveowners(request):
    s=oreg.objects.filter(status='pending')
    context={'key':s}
    template = loader.get_template("approveowner.html")
    return HttpResponse(template.render(context, request))

def approveveg(request):
    s=vegdet.objects.raw("select shop_vegdet.*,admin_oreg.name,admin_category.cname from shop_vegdet,admin_oreg,admin_category where shop_vegdet.oid=admin_oreg.id and shop_vegdet.category=admin_category.id and shop_vegdet.status='pending'")
    context={'key':s}
    template = loader.get_template("approveveg.html")
    return HttpResponse(template.render(context, request))
def approveuser(request,id):
    u=ureg.objects.get(id=id)
    u.status='approve'
    u.save()
    return HttpResponse("<script>alert('Customer approved successfully');window.location='/approveusers';</script>")
def rejectuser(request,id):
    u=ureg.objects.get(id=id)
    u.status='reject'
    u.save()
    return HttpResponse("<script>alert('Customer rejected successfully');window.location='/approveusers';</script>")
def approveowner(request,id):
    u=oreg.objects.get(id=id)
    u.status='approve'
    u.save()
    return HttpResponse("<script>alert('Shop approved successfully');window.location='/approveowners';</script>")
def rejectowner(request,id):
    u=oreg.objects.get(id=id)
    u.status='reject'
    u.save()
    return HttpResponse("<script>alert('Shop rejected successfully');window.location='/approveowners';</script>")
def approvevegs(request,id):
    v=vegdet.objects.get(id=id)
    v.status='approve'
    v.save()
    return HttpResponse("<script>alert('Items approved successfully');window.location='/approveveg';</script>")
def rejectveg(request,id):
    v=vegdet.objects.get(id=id)
    v.status='reject'
    v.save()
    return HttpResponse("<script>alert('Items rejected successfully');window.location='/approveveg';</script>")
def banking(request):
    context = {}
    template = loader.get_template("banking.html")
    return HttpResponse(template.render(context, request))
def addbank(request):
    if request.method == "POST":

        bname=request.POST.get("bname")
        logo=request.FILES["logo"]

        s1=Bank.objects.all()
        for i in s1:
            if(i.bname == bname):
                return HttpResponse("<script>alert('already exist');window.location='/addbank';</script>")
        else:
            s=Bank()
            s.bname=bname
            s.logo=logo
            s.save()
            return HttpResponse("<script>alert('bank name added successfully');window.location='/addbank';</script>")
    else:
        context = {}
        template = loader.get_template("AddBank.html")
        return HttpResponse(template.render(context, request))
def addaccount(request):
    if request.method == "POST":
        bname = request.POST.get("drpbank")
        bankid = Bank.objects.get(id=bname)
        brname = request.POST.get("drpbranch")
        branchid = Branch.objects.get(id=brname)
        cname = request.POST.get("cname")
        cno = request.POST.get("cno")
        cvv = request.POST.get("cvv")
        year = request.POST.get("year")
        month = request.POST.get("month")
        amount = request.POST.get("amount")
        s = Account()

        s.cname = cname
        s.cno = cno
        s.cvv = cvv
        s.amount = amount
        s.year = year
        s.month = month
        s.bname = bankid.id
        s.branch = branchid.id
        s.save()
        return HttpResponse("<script>alert('account added successfully');window.location='/addaccount';</script>")
    else:
        b = Bank.objects.all()
        template = loader.get_template("AddAccount.html")
        context = {'bank': b}
        return HttpResponse(template.render(context, request))
def brnch(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        did = request.GET.get('q')
        l = Branch.objects.filter(bname=did).values()
        return JsonResponse(list(l), safe=False)


def addbranch(request):
    if request.method=="POST":
        bn=request.POST.get("drpbname")
        bid=Bank.objects.get(id=bn)
        brname=request.POST.get("branch")
        addr = request.POST.get("addr")
        ifsc = request.POST.get("ifsc")
        email = request.POST.get("email")
        phno = request.POST.get("phno")
        s=Branch()
        s.branch=brname
        s.address=addr
        s.email=email
        s.phone=phno
        s.ifsc=ifsc
        s.bname=bid.id
        s.save()
        return HttpResponse("<script>alert('branch added successfully');window.location='/addbranch';</script>")
    else:
        s = Bank.objects.all()
        template = loader.get_template("AddBranch.html")
        context = {'bank': s}
        return HttpResponse(template.render(context, request))

def adminvieworders(request):


    o=order_child.objects.raw("select distinct(admin_ureg.name),admin_ureg.location,admin_ureg.lmark,admin_ureg.phone,customer_order_master.* from admin_ureg,customer_order_master,customer_order_child,shop_vegdet,admin_oreg where admin_ureg.id=customer_order_master.uid and customer_order_master.id=customer_order_child.oid and customer_order_child.vid=shop_vegdet.id and shop_vegdet.oid=admin_oreg.id  ")
    context = {'key': o}
    template = loader.get_template("adminvieworders.html")
    return HttpResponse(template.render(context, request))

def adminvieworders1(request,id):


    o=order_child.objects.raw("select customer_order_child.*,admin_category.cname,shop_vegdet.vegname,shop_vegdet.rate from customer_order_master,customer_order_child,shop_vegdet,admin_category where customer_order_master.id=customer_order_child.oid and customer_order_child.vid=shop_vegdet.id and shop_vegdet.category=admin_category.id and customer_order_master.id=%s",[id])
    context = {'key': o}
    template = loader.get_template("adminvieworders1.html")
    return HttpResponse(template.render(context, request))