from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from company.models import Company, Company_skills,Company_notice
from django.urls import reverse
from datetime import datetime
import json
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from student.views import studentlist
from student.models import Student,Academicprofile,Skills,Project,Internship

# Create your views here.
def index(request):
    return render(request,'company/homepage.html')
def signup(request):
    return render(request,'company/signup.html')

def companyreg(request):
    return render(request,'company/companyreg.html')


def companyregsub(request):
    name=request.POST['name']
    password=request.POST['password']
    username=request.POST['username']
    email=request.POST['email']
    city=request.POST['city']
    country=request.POST['country']
    websiteurl=request.POST['wurl']
    description=request.POST['des']
    usercount=Company.objects.filter(username=username).count()
    skilllist=['python','java','dotnet','c++','android','iot','machine learning','r programming','database','big data','data structure','ios','networking','frontend','backend','django','laravel','js frameworks']

    if usercount>=1:
        #return render(request,'freeusers/signup.html',{'message': 'username exists'})
        return HttpResponseRedirect(reverse('companyreg') + '?auth=true')
    else:
        c=Company(name=name,username=username,password=password,email=email,city=city,country=country,websiteurl=websiteurl,description=description)
        c.save()
        c1=Company.objects.get(username=username)
        cn=Company_notice(company_unam=c1,internships='',placements='')
        cn.save()
        '''if 'python' in request.POST:
            return HttpResponse('yes')'''
        comp=Company.objects.get(username=username)
        for skills in skilllist:
            if skills in request.POST:
                sk= request.POST[skills]
                sk=Company_skills(skill=sk,company_uname=comp)
                sk.save()


        return HttpResponseRedirect(reverse('login') )

def companyprofile(request):
    current=datetime.now()
    hour=current.hour
    if hour >=0 and hour <12:
        message='Good Morning'
    elif hour>=12 and hour<16:
        message='Good Afternoon'
    else:
        message='Good Evening'
    print(message)
    username=request.session['username']
    c=Company.objects.get(username=username)#we get a row
    id = c.id
    n = Company_notice.objects.get(company_unam=id)
    return render(request,'company/companyprofile.html',{
    'username':username,
    'messageoftheday':message,
    'company':c,
    'notice':n
    })

def companyprofileupdate(request):
    username=request.session['username']
    c=Company.objects.get(username=username)#we get a row



    li=[]

    l=Company_skills.objects.filter(company_uname_id=c.id)
    for i in l:
        li.append(i.skill)
    #tt = json.dumps(li, cls=DjangoJSONEncoder)




    return render(request,'company/companyprofileupdate.html',{'company':c,'skills':li})

def companyupdatesubmit(request):
    username=request.session['username']
    name=request.POST['name']


    email=request.POST['email']
    city=request.POST['city']
    country=request.POST['country']
    websiteurl=request.POST['wurl']
    description=request.POST['des']
    usercount=Company.objects.filter(username=username).count()
    skilllist=['python','java','dotnet','c++','android','iot','machine learning','r programming','database','big data','data structure','ios','networking','frontend','backend','django','laravel','js frameworks']
    c=Company.objects.get(username=username)
    ck=Company.objects.filter(username=username)
    ck.update(name=name,email=email,city=city,country=country,websiteurl=websiteurl,description=description)
    comp=Company.objects.get(username=username)
    Company_skills.objects.filter(company_uname_id=c.id).delete()
    for skills in skilllist:
        if skills in request.POST:
            sk= request.POST[skills]
            s=Company_skills(skill=sk,company_uname=comp)
            s.save()

    return HttpResponseRedirect(reverse(companyprofile)+ '?auth=true')

def companynotice(request):
    return render(request,'company/companynotice.html')

def noticesubmit(request):
    username=request.session['username']
    c = Company.objects.get(username = username)
    internships = request.POST['internships']
    placements = request.POST['placements']

    cn = Company_notice.objects.filter(company_unam = c)

    if len(cn)<=0:
        cnn=Company_notice(internships=internships,placements=placements,company_unam=c)
        cnn.save()
    #intern = cn.internships
    #place = cn.placements
    #intern = intern +'\n'+internships
    #place = place +'\n'+placements
    else:
        ccn = Company_notice.objects.get(company_unam = c)
        ccn.internships = internships
        ccn.placements = placements
        ccn.save()
    #cn.update(internships = intern,placements = place)
    #cn = Company_notice(internships = internships,placements=placements,company_unam = c)
    #cn.save()
    return HttpResponseRedirect(reverse('companyprofile'))





'''def sendmail(request):
    redranks=request.session['reducedskills']
    li = []
    li1=[]
    for r in redranks:
        email = (Student.objects.get(id=r.id)).email
        li.append(email)

    subject = 'Eligible for interview'
    message = 'Hey,man you are eligible for interview.Now come all guns blazing.All the best!!'
    from_email = settings.EMAIL_HOST_USER


    a=send_mail(subject,message,from_email,li,fail_silently = True)
    print(li1)
    return HttpResponse('success')'''


def selectstudents(request):

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


    return render(request,'company/selectstudents.html',{
    'rank_object':rank_object,
    'rank':rank,
    'dict1':dict1,
    'slist':ls,
    'listrank':lsrank,
    'name':name,
    'student':ls,

    })

    #return render(request,'company/selectstudents.html')

def studentfilter(request):
    skilllist=['python','java','dotnet','c','android','iot','machine learning','r programming','database','big data','data structure','ios','networking','frontend','backend','django','laravel','js frameworks']
    slist=[]


    for skills in skilllist:
        if skills in request.POST:
            sk= request.POST[skills]

            s=Skills.objects.filter(skill=sk) # take students with skill in list
            for i in s:
                slist.append(i.student_id)
    print(slist)
    sset=set(slist)
    print(sset)
    ranksred=[]
    ranks=Academicprofile.objects.all().order_by('-sum')
    for obj in ranks:
        if obj.student_id in sset:
            ranksred.append(obj)

    rank={}
    rank_object={}
    i=1
    for r in ranksred:
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
    for r in ranksred:
        ss=Student.objects.get(id=r.student_id)
        dict1[r.student_id]=ss.name
        ls.append(ss)
        lsrank.append(listrank)
        listrank+=1
        name.append(ss.name)
        uname.append(ss.username)


    return render(request,'company/selectstudents.html',{
    'rank_object':rank_object,
    'rank':rank,
    'dict1':dict1,
    'slist':ls,
    'listrank':lsrank,
    'name':name,
    'student':ls,

    })
