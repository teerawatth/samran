from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',sign_in,name='login'),
    path('logout/',sign_out,name='logout'),
    path('profile/',profile,name='profile'),
    path('editprofile/',editprofile,name='editprofile'), 
    path('booking/<int:id>/',booking,name='booking'), 
    path('booking_list/',booking_list,name='booking_list'), 
    path('permissions/<int:id>/',permissions,name='permissions'),
    path('permissions_no/<int:id>/',permissions_no,name='permissions_no'),
    path('reset/',reset,name='reset'),
]