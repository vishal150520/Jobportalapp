
from django.urls import path
from . import views
from .views import logout,addjob1,savejob1,uptjob1,jobupdate1,jobdel1,jobdell1,viewjob1,cm2,ucd1,ucd3
urlpatterns=[
    path('9/',logout,name='logout'),
    path('10/',addjob1,name='addjob'),
    path('11/',savejob1,name='jobsave'),
    path('12/',uptjob1,name='uptjob'),
    path('13/',jobupdate1,name='jobupdate'),
    path('14/',jobdel1,name='deljob'),
    path('15',jobdell1,name='jobdell'),
    path('16',viewjob1,name='viewjob'),
    path('17/',cm2,name='cm1'),
    path('18/',ucd1,name='ucd'),
    path('19/',ucd3,name='ucd2'),
]