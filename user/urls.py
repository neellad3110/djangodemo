from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.index,name="index-page"),  
    path('home/',views.home, name='home'),
    path('register/',views.userregister, name='register-page'),
    path('login/',views.userlogin, name='login-page'),
    path('logout/',views.userlogout, name='logout-page'),

    
]