from operator import imod
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import projections
import mysql.connector
from django.contrib.auth import authenticate

from home.models import candidate, company

# Create your views here.
def index(request):
    return render(request,'home1.html')
def canlog(request):
    return render(request,'candidatelogin.html')
def cansign(request):
    return render(request,'candidatesignup.html')
def comlog(request):
    return render(request,'companylogin.html')
def comsign(request):
    return render(request,'companysignup.html')
def cansign1(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        dateofbirth=request.POST.get('dateofbirth')
        qualification=request.POST.get('qualification')
        percentage=request.POST.get('percentage')
        skills=request.POST.get('skills')
        email=request.POST.get('email')
        contactno=request.POST.get('contactno')
        password=request.POST.get('password')
        projectd=request.POST.get('projectd')
        o=candidate(firstName=fname,lastName=lname,gender=gender,dateofbirth=dateofbirth,qualification=qualification,percentage=percentage,skills=skills,email=email,contactno=contactno,password=password,projectdetails=projectd)
        o.save()
        n="data inserted"
    return render(request,'home1.html',{'n':n})
def comsign1(request):
    if request.method=='POST':
        cn=request.POST.get('cn')
        cgstno=request.POST.get('cgstno')
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        empid=request.POST.get('empid')
        contact=request.POST.get('contact')
        mail=request.POST.get('email')
        password=request.POST.get('pass')
        jd=request.POST.get('jd')
        o=company(companyname=cn,companygstno=cgstno,hrmfname=fn,hrmlname=ln,dateofbirth=dob,gender=gender,empid=empid,contactno=contact,email=mail,password=password,jobdescription=jd)
        o.save()
        n="data inserted"
    return render(request,'home1.html',{'n':n})
def comlog1(request):
    return HttpResponse("this is com log inn")
def canlog1(request):
    if request.method=='POST':
        user=request.POST.get('user1')
        pass1=request.POST.get('pass1')
        cur=connection.cursor()
        h="select 1 from home_candidate where email='"+user+"' AND password='"+pass1+"';"
        cur.execute(h)
        if not cur.fetchmany():
            return HttpResponse('not')
        else:
            n="Sucessfully Login '"+user+"'"
            return render(request,'candidatehome.html',{'n':n})
    
def comlog1(request):
    if request.method=='POST':
        user=request.POST.get('user')
        passw=request.POST.get('pass')
        cur=connection.cursor()
        h="select 1 from home_company where email='"+user+"' AND password='"+passw+"';"
        cur.execute(h)
        if not cur.fetchmany():
            return HttpResponse('not')
        else:
            n="Sucessfully Login '"+user+"'"
            return render(request,'companyhome.html',{'n':n})
