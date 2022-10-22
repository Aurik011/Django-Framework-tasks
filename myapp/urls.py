from django.urls import path, re_path

from . import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    # path('register/',views.register, name='register') 
    # module 'myapp.views' has no attribute 'register'
    # Error solution: There is double quote on register above this line
    # path('facility/',views.facility, name='facility')
    # path('members/',views.members, name='members')
    # path('contactus/',views.contactus, name='contactus')

]

