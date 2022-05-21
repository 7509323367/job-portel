from django.urls import path
from .import views 
urlpatterns=[
     path('jobinfo',views.jobinfo,name='jobinfo'),   
     path('hrreg',views.hrreg,name='hrreg'),
     path('job',views.job,name='job'),
     path('candidate',views.candidate,name='candidate'),
     path('registration',views.registration,name='registration'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('home',views.home,name='home'),
]