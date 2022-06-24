from django.urls import path
from . import views
from .views  import  canlog,cansign,comlog,comsign,cansign1,comsign1,comlog1,canlog1
urlpatterns=[
    path('',views.index,name='index'),
    path('1/',canlog,name='template1'),
    path('2/',cansign,name='template2'),
    path('3/',comlog,name='template3'),
    path('4/',comsign,name="template4"),
    path('5/',cansign1,name='temp1'),
    path('6/',comsign1,name='temp2'),
    path('7/',comlog1,name='temp3'),
    path('8/',canlog1,name='temp4'),
    
   
]