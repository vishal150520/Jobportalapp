from fnmatch import fnmatchcase
from django.shortcuts import render
from django.db import connection
from setuptools import find_namespace_packages
from urllib3 import Retry

from company.models import joblist
from home.models import company
# Create your views here.
def logout(request):
    return render(request,'home1.html')
def addjob1(request):
    return render(request,'addjob.html')
def savejob1(request):
    if request.method=='POST':
        jobid=request.POST.get('jobid')
        jobd=request.POST.get('jobd')
        cur=connection.cursor()
        o=joblist(jobid=jobid,jobdesc=jobd)
        o.save()
        n="data inserted"
    return render(request,'companyhome.html',{'n':n})

def uptjob1(request):
    return render(request,'uptjob.html')
def jobupdate1(request):
    if request.method=='POST':
        jobid=request.POST.get('jobid')
        jobd=request.POST.get('jobd')
        t=joblist.objects.get(jobid=jobid)
        t.jobdesc=jobd
        t.save()
    n="Update Suceessfully"
    return render(request,'companyhome.html',{'n':n})
def jobdel1(request):
    return render(request,'deljob.html')

def jobdell1(request):
    if request.method=='POST':
        jobid=request.POST.get('jobid')
        o=joblist.objects.get(jobid=jobid)
        o.delete()
    n="delete Suceessfully"
    return render(request,'companyhome.html',{'n':n})
def viewjob1(request):
    data=joblist.objects.all()
    return render(request,'viewjob.html',{'data':data})
def cm2(request):
    return render(request,'companyhome.html')
def ucd1(request):
    return render(request,'ucd.html')
def ucd3(request):
    if request.method=='POST':
        cn1=request.POST.get('cn')
        cgstno1=request.POST.get('cgstno')
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        empid=request.POST.get('empid')
        contact=request.POST.get('contact')
        mail=request.POST.get('email')
        password=request.POST.get('pass')
        jd=request.POST.get('jd')
        o=company.objects.get(companyname=cn1)
        o.companyname=cn1
        o.companygstno=cgstno1
        o.hrmfname=fn
        o.hrmlname=ln
        o.dateofbirth=dob
        o.gender=gender
        o.empid=empid
        o.contactno=contact
        o.email=mail
        o.password=password
        o.jobdescription=jd
        o.save()
        n="data update"
    return render(request,'home1.html',{'n':n})