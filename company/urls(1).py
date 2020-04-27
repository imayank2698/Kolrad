from django.urls import path
from . import views


urlpatterns = [
        path('',views.index,name='index'),
        path('signup/',views.signup,name='signup'),
        path('companyreg/',views.companyreg,name='companyreg'),
        path('companyregsub/',views.companyregsub,name='companyregsub'),
        path('companyprofile/',views.companyprofile,name='companyprofile'),
        path('companyprofileupdate/',views.companyprofileupdate,name='companyprofileupdate'),
        path('companyupdatesubmit/',views.companyupdatesubmit,name='companyupdatesubmit'),
        path('companynotice/',views.companynotice,name='companynotice'),
        path('noticesubmit/',views.noticesubmit,name='noticesubmit'),
        #path('sendmailtest/',views.sendmailtest,name = 'sendmailtest'),
        path('selectstudents/',views.selectstudents,name = 'selectstudents'),
        path('studentfilter/',views.studentfilter,name='studentfilter'),
        #path('sendmail/',views.sendmail,name='sendmail')


]
