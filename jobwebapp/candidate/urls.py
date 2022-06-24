from django.urls import path
from . import views
from .views import afajob1,applyjob1,acl1,ucd2,ucand2
urlpatterns=[
   
    path('20/',afajob1,name='afajob'),
    path('21/',applyjob1,name='applyjob'),
    path('22/',acl1,name='acl'),
    path('23/',acl1,name='lwca'),
    path('24/',ucd2,name='ucd1'),
    path('25/',ucand2,name='ucand1')
]