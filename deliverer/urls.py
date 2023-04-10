
from django.urls import path
import deliverer.views
urlpatterns = [
    path('shome/',deliverer.views.staffhome),
    path('staffvieworderdetails/', deliverer.views.staffvieworders, name='staffvieworderdetails'),
    path('staffvieworders1/<id>', deliverer.views.staffvieworders1, name='staffvieworders1'),
    path('updatestatus/',deliverer.views.updatestatus,name='updatestatus'),
    path('updatestock/', deliverer.views.updatestock, name='updatestock'),
    path('us/', deliverer.views.us, name='us')

]