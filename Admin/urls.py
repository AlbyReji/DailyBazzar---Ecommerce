
from django.urls import path
import Admin.views
urlpatterns = [
    path('login/', Admin.views.login1, name='login1'),
    path('', Admin.views.index, name='index'),
    path('admin1/', Admin.views.admin1, name='admin1'),
    path('category/', Admin.views.category1, name='category'),
    path('staff/', Admin.views.staff1, name='staff'),
    path('approveusers/', Admin.views.approveusers, name='uapprove'),
    path('approveowners/', Admin.views.approveowners, name='oapprove'),
    path('approveveg/', Admin.views.approveveg, name='approveveg'),
    path('approveuser/<id>', Admin.views.approveuser, name='approveuser'),
    path('rejectuser/<id>', Admin.views.rejectuser, name='rejectuser'),
    path('approveowner/<id>', Admin.views.approveowner, name='approveowner'),
    path('rejectowner/<id>', Admin.views.rejectowner, name='rejectowner'),
    path('approvevegs/<id>', Admin.views.approvevegs, name='approvevegs'),
    path('rejectveg/<id>', Admin.views.rejectveg, name='rejectveg'),
    path('banking/', Admin.views.banking, name='banking'),
    path('addbank/', Admin.views.addbank, name='bank'),
    path('addbranch/', Admin.views.addbranch, name='branch'),
    path('addaccount/', Admin.views.addaccount, name='account'),
    path('brnch/', Admin.views.brnch, name='brnch'),
    path('adminvieworders/', Admin.views.adminvieworders, name='adminvieworders'),
    path('adminvieworders1/<id>', Admin.views.adminvieworders1, name='adminvieworders1'),

]