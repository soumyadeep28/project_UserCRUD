from django.urls import path
from . import views
urlpatterns = [ 
    path('' , views.home , name ="home") ,
    path('loginuser/' , views.signinpage , name='login'),
    path('register/' , views.register , name='register'),
    path('dashboard/' , views.dashboard , name ="dashboard") ,

]