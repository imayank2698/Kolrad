from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.urls import reverse #we used reverse function to use name instead of a url in urls.py
from django.core.files.storage import FileSystemStorage
#from rank import DenseRank,UpperRank,Rank
from company.models import Company,Company_notice
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from math import *
# Create your views here.

from student.models import Student,Academicprofile,Skills,Project,Internship

def register(request):
    return render(request,'student/register.html')

def registeraction(request):
    name=request.POST.get('name','NULL')
    email=request.POST.get('email','NULL')
    contact=request.POST.get('phone','NULL')
    username=request.POST.get('username','NULL')
    password=request.POST.get('password','NULL')
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)

    bool=usernamepresent(username)
    if contact=='NULL':
        contact=0
    if bool==True:
        s=Student(name=name,email=email,contact=contact,username=username,password=password,pic_path=uploadedfileurl)

        s.save()
        if s.id:
            subject = 'Registered'
            message = 'Thank you for Registering -Kolrad Inc'
            from_email = settings.EMAIL_HOST_USER
            li=[email]

            a=send_mail(subject,message,from_email,li,fail_silently = True)

            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse('Error')

    else:
        return HttpResponseRedirect(reverse('studentregister')+'?auth1=true')
        #return render(request,'student/register.html')

def usernamepresent(username):
    if Student.objects.filter(username=username).exists():
        return False
    else:
        return True

def login(request):
    return render(request,'student/login.html')

def authenticate(request):
        username=request.POST['username']
        password=request.POST['password']

        l=Student.objects.filter(username=username,password=password)

        if len(l):
            request.session['username']=username #session started
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            c=Company.objects.filter(username=username,password=password)
            if len(c):
                request.session['username']=username
                return HttpResponseRedirect(reverse('companyprofile'))
            else:
                return HttpResponseRedirect(reverse('login')+'?login_failure=true')

def dashboard(request):
    username=request.session['username']
    current=datetime.now()
    hour=current.hour
    if hour >=0 and hour <12:
        message='Good Morning'
    elif hour>=12 and hour<16:
        message='Good Afternoon'
    else:
        message='Good Evening'
    print(message)

    s=Student.objects.get(username=username)#we get a row

    return render(request,'student/dashboard.html',{
    'username':username,
    'messageoftheday':message,
    'student':s
    })

def academic(request):
    return render(request,'student/academic.html')

def academicauth(request):
    ssc=request.POST.get('ssc','NULL')
    hsc=request.POST.get('hsc','NULL')
    cgpa=request.POST.get('cgpa','NULL')
    division=request.POST.get('division','NULL')
    department=request.POST.get('department','NULL')
    rollno=request.POST.get('roll_no','NULL')
    desc=request.POST.get('comment','NULL')

    if cgpa=='NULL':
        cgpa=0

    result=''
    if cgpa=='2':
        result='<7'
    if cgpa=='4':
        result='7-7.5'
    if cgpa=='6':
        result='7.5-8.5'
    if cgpa=='8':
        result='8.5-9'
    if cgpa=='10':
        result='9-10'

    sum=int(cgpa)
    username=request.session['username']
    s = Student.objects.get(username=username)

    ac=Academicprofile(ssc=ssc,hsc=hsc,cgpa=result,department=department,division=division,rollno=rollno,desc=desc,sum=sum,student=s)

    ac.save()

    return HttpResponseRedirect(reverse('dashboard'))

def internship(request):
    return render(request,'student/internship.html')

def internshipauth(request):
    internship=request.POST.get('internship','NULL')
    desc=request.POST.get('comment','NULL')
    name=request.POST.get('name','NULL')
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)
        username=request.session['username']
        s = Student.objects.get(username=username)
    i=Internship(type=internship,name=name,desc=desc,pic_path=uploadedfileurl,student=s)
    i.save()

    return HttpResponseRedirect(reverse('dashboard'))

def project(request):
    return render(request,'student/project.html')

def projectauth(request):
    projectname=request.POST.get('projectname','NULL')
    github=request.POST.get('github','NULL')
    desc=request.POST.get('comment','NULL')
    username=request.session['username']
    s = Student.objects.get(username=username)
    p=Project(projectname=projectname,github=github,desc=desc,student=s)
    p.save()
    return HttpResponseRedirect(reverse('dashboard'))

def skills(request):
    return render(request,'student/skills.html')

def skillsauth(request):
    skills=request.POST.get('skills','NULL')
    rate=request.POST.get('rate','NULL')
    rate=int(rate)
    username=request.session['username']

    s = Student.objects.get(username=username)
    sk=Skills.objects.filter(student_id=s.id,skill=skills)
    if len(sk)>=1:
        sk.update(rate=rate)
    else:
        p=Skills(skill=skills,rate=rate,student=s)
        p.save()

    return HttpResponseRedirect(reverse('dashboard'))

def logout(request):
    request.session.flush()

    return HttpResponseRedirect(reverse('login'))

def profile(request):
    username=request.session['username']
    s = Student.objects.get(username=username)
    skills=Skills.objects.filter(student_id=s.id)
    internships=Internship.objects.filter(student_id=s.id,type='internship')
    certifications=Internship.objects.filter(student_id=s.id,type='certification')
    print(certifications)
    projects=Project.objects.filter(student_id=s.id)
    a=Academicprofile.objects.get(student_id=s.id)
    sum=0
    if a.cgpa=='<7':
        cgpa=2
    if a.cgpa=='7-7.5':
        cgpa=4
    if a.cgpa=='7.5-8.5':
        cgpa=6
    if a.cgpa=='8.5-9':
        cgpa=8
    else:
        cgpa=10

    sum=cgpa+(len(internships))*10+(len(projects))*5

    print("sum=",sum)

    Academicprofile.objects.filter(student_id=s.id).update(sum=sum)

    ranks=Academicprofile.objects.all().order_by('-sum')
    rank={}
    rank_object={}
    i=1
    for r in ranks:
        rank[r.student_id]=i
        rank_object[i]=r.student_id
        i+=1
    acad=Academicprofile.objects.get(student_id=s.id)
    return render(request,'student/profile.html',{
        'student':s,
        'skills':skills,
        'internships':internships,
        'projects':projects,
        'username':username,
        'certifications':certifications,
        'rank':rank[s.id],
        'acad':acad,
    })

def studentlist(request):
    #Academicprofile.objects.filter(student_id=s.id).update(sum=sum)
    username=request.session['username']
    ranks=Academicprofile.objects.all().order_by('-sum')
    rank={}
    rank_object={}
    i=1
    for r in ranks:
        rank[r.student_id]=i
        rank_object[i]=r.student_id
        i+=1
    s = Student.objects.all()
    dict1={}
    ls=[]
    lsrank=[]
    listrank=1
    name=[]
    uname=[]
    for r in ranks:
        ss=Student.objects.get(id=r.student_id)
        dict1[r.student_id]=ss.name
        ls.append(ss)
        lsrank.append(listrank)
        listrank+=1
        name.append(ss.name)
        uname.append(ss.username)


    return render(request,'student/studentlist.html',{
    'rank_object':rank_object,
    'rank':rank,
    'dict1':dict1,
    'slist':ls,
    'listrank':lsrank,
    'name':name,
    'student':ls
    })

def studentprofile(request,username):

        s = Student.objects.get(username=username)
        skills=Skills.objects.filter(student_id=s.id)
        internships=Internship.objects.filter(student_id=s.id,type='internship')
        certifications=Internship.objects.filter(student_id=s.id,type='certification')
        print(certifications)
        projects=Project.objects.filter(student_id=s.id)
        a=Academicprofile.objects.get(student_id=s.id)
        sum=0
        if a.cgpa=='<7':
            cgpa=2
        if a.cgpa=='7-7.5':
            cgpa=4
        if a.cgpa=='7.5-8.5':
            cgpa=6
        if a.cgpa=='8.5-9':
            cgpa=8
        else:
            cgpa=10

        sum=cgpa+(len(internships))*10+(len(projects))*5

        print("sum=",sum)

        Academicprofile.objects.filter(student_id=s.id).update(sum=sum)

        ranks=Academicprofile.objects.all().order_by('-sum')
        rank={}
        rank_object={}
        i=1
        for r in ranks:
            rank[r.student_id]=i
            rank_object[i]=r.student_id
            i+=1
        acad=Academicprofile.objects.get(student_id=s.id)
        return render(request,'student/profile.html',{
            'student':s,
            'skills':skills,
            'internships':internships,
            'projects':projects,
            'username':username,
            'certifications':certifications,
            'rank':rank[s.id],
            'acad':acad,
        })

def companyview(request,username):
    c=Company.objects.get(username=username)
    cn=Company_notice.objects.get(company_unam=c.id)
    return render(request,'student/companyview.html',{
    'company':c,
    'username':username,
    'notice':cn,
    })

def companylist(request):
    c=Company.objects.all()
    return render(request,'student/companylist.html',{
    'company':c,
    })

def registerupdate(request):
    username=request.session['username']
    s=Student.objects.get(username=username)
    return render(request,'student/registerupdate.html',{
        's':s
    })


def academicupdate(request):
    username=request.session['username']
    s=Student.objects.get(username=username)
    a=Academicprofile.objects.get(student_id=s.id)
    return render(request,'student/academicupdate.html',{
        'a':a,
    })


def registerupdateauth(request):
    username=request.session['username']
    s=Student.objects.filter(username=username)
    name=request.POST.get('name','NULL')
    email=request.POST.get('email','NULL')
    contact=request.POST.get('phone','NULL')
    s.update(name=name,email=email,contact=contact)
    return HttpResponseRedirect(reverse('dashboard'))



def academicupdateauth(request):
    username=request.session['username']
    s=Student.objects.get(username=username)
    a=Academicprofile.objects.filter(student_id=s.id)
    ssc=request.POST.get('ssc','NULL')
    hsc=request.POST.get('hsc','NULL')
    cgpa=request.POST.get('cgpa','NULL')
    division=request.POST.get('division','NULL')
    department=request.POST.get('department','NULL')
    rollno=request.POST.get('roll_no','NULL')
    desc=request.POST.get('comment','NULL')

    if cgpa=='NULL':
        cgpa=0

    result=''
    if cgpa=='2':
        result='<7'
    if cgpa=='4':
        result='7-7.5'
    if cgpa=='6':
        result='7.5-8.5'
    if cgpa=='8':
        result='8.5-9'
    if cgpa=='10':
        result='9-10'

    sum=int(cgpa)

    a.update(ssc=ssc,hsc=hsc,cgpa=cgpa,division=division,department=department,rollno=rollno,desc=desc,sum=sum)
    return HttpResponseRedirect(reverse('dashboard'))

def cover(request):
    return render(request,'student/index.html')
