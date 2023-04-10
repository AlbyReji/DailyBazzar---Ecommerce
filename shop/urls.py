
from django.urls import path
import shop.views
urlpatterns = [
path('oreg/', shop.views.oreg1, name='oreg'),
    path('veg/', shop.views.veg1, name='veg'),
    path('ohome/', shop.views.ownerhome, name='ohome'),
    path('vieworderdetails/', shop.views.vieworders, name='vieworderdetails'),
    path('vieworders1/<id>', shop.views.vieworders1, name='vieworders1'),
    path('assignorder/', shop.views.assignorder, name='assignorder'),
    path('vieworderstatus/',shop.views.vieworderstatus, name='vieworderstatus'),
    path('vieworderstatus1/<id>', shop.views.vieworderstatus1, name='vieworderstatus1'),
    path('viewstock/', shop.views.viewstock, name='viewstock'),
    path('editveg/', shop.views.editveg, name='editveg'),
    path('editveg1/<id>', shop.views.editveg1, name='editveg1'),
    path('deleteveg/<id>', shop.views.deleteveg, name='deleteveg'),
    path('editveg2/', shop.views.editveg2, name='editveg2'),


]