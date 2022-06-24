from django.http import HttpResponse
from django.shortcuts import render
from urllib3 import Retry
from candidate.models import applyjob
from home.models import candidate
# Create your views here.
def afajob1(request):
    return render(request,'applyjob.html')
def applyjob1(request):
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
        jobid=request.POST.get('jobid')
        projectd=request.POST.get('pd')
        o=applyjob(firstName=fname,lastName=lname,gender=gender,dateofbirth=dateofbirth,qualification=qualification,percentage=percentage,skills=skills,email=email,contactno=contactno,jonid=jobid,projectdetails=projectd)
        o.save()
        n="sucessfully applied"
    return render(request,'candidatehome.html',{'n':n})
def acl1(request):
    data=applyjob.objects.all()
    return render(request,'applyjoblist.html',{'data':data})
def ucd2(request):
    return render(request,'ucand.html')
def ucand2(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender1=request.POST.get('gender')
        dateofbirth=request.POST.get('dateofbirth')
        qualification=request.POST.get('qualification')
        percentage=request.POST.get('percentage')
        skills=request.POST.get('skills')
        email=request.POST.get('email')
        contactno=request.POST.get('contactno')
        password1=request.POST.get('password')
        projectd=request.POST.get('projectd')
        o=candidate.objects.get(firstname=fname)
        o.firstname=fname
        o.lastname=lname
        o.gender=gender1
        o.dateofbirth=dateofbirth
        o.qualification=qualification
        o.percentage=percentage
        o.email=email
        o.skills=skills
        o.contactno=contactno
        o.password=password1
        o.projectdetails=projectd
        o.save()
        n="data update"
    return render(request,'home1.html',{'n':n})