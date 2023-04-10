
from django.urls import path
import customer.views
urlpatterns = [
path('ureg/', customer.views.ureg1, name='ureg'),
    path('uhome/', customer.views.userhome, name='uhome'),
    path('searchitems/', customer.views.searchitems, name='searchitems'),
    path('searchitems1/<id>', customer.views.searchitems1, name='searchitems1'),
    path('addcart/', customer.views.addcart, name='addcart'),
    path('deletecart/<id>', customer.views.deletecart, name='deletecart'),
    path('viewcart/', customer.views.viewcart, name='viewcart'),
    path('payment/', customer.views.payment, name='payment'),
    path('paymentcon/',customer.views.paymentcon,name='paymentcon'),
    path('savepayment/', customer.views.savepayment, name='savepayment'),
    path('uservieworderstatus/',customer.views.uservieworderstatus, name='uservieworderstatus'),
    path('uservieworderstatus1/<id>', customer.views.uservieworderstatus1, name='uservieworderstatus1'),
    path('cancelorder/', customer.views.cancelorder, name='cancelorder'),
    path('cancelorder1/<id>', customer.views.cancelorder1, name='cancelorder1'),
    path('cancelorder2/', customer.views.cancelorder2, name='cancelorder2'),

]