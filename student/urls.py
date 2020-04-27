from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('register/',views.register,name="studentregister"),
path('registerauth/',views.registeraction,name="registeraction"),
path('login/',views.login,name='login'),
path('auth/',views.authenticate,name='authenticateuser'),
path('dashboard/',views.dashboard,name='dashboard'),
path('academic/',views.academic,name="academic"),
path('academicauth/',views.academicauth,name='academicauth'),
path('internship/',views.internship,name='internship'),
path('internshipauth/',views.internshipauth,name='internshipauth'),
path('project/',views.project,name='project'),
path('projectauth/',views.projectauth,name='projectauth'),
path('skills/',views.skills,name='skills'),
path('skillsauth/',views.skillsauth,name='skillsauth'),
path('logout/',views.logout,name='logout'),
path('profile/',views.profile,name='profile'),
path('studentlist/',views.studentlist,name='studentlist'),
path('studentprofile/<str:username>',views.studentprofile,name='studentprofile'),
path('companyview/<str:username>',views.companyview,name='companyview'),
path('companylist/',views.companylist,name='companylist'),
path('registerupdate/',views.registerupdate,name='registerupdate'),
path('academicupdate/',views.academicupdate,name='academicupdate'),
path('registerupdateauth/',views.registerupdateauth,name='registerupdateauth'),
path('academicupdateauth/',views.academicupdateauth,name='academicupdateauth'),
path('cover/',views.cover,name='cover')
]
