from django.urls import path
from .views import transfer_funds
from . import views

urlpatterns = [
    path('',views.test),
    path('login',views.login),
    path('log',views.log),
    path('register',views.register),
    path('input',views.input),
    path('Welcome',views.Welcome),
    path('home',views.home),
    path('aboutus',views.aboutus),
    path('accshow',views. accshow),
    path('adminlogin',views.adminlogin),
    path('adminapoorve',views.adminapoorve),
    path('adminlog',views.adminlog),
    path('adminregister',views.adminregister),
    path('admininput',views.admininput),
    path('initial',views.initial),
    path('approve',views.approve),
    # path('initialbalance',views.initialbalance),
    path('initialbalance/', views.initialbalance, name='initialbalance'),
    path('show',views.show),
    path('vieww',views.vieww),
    path('adminview',views.adminview),
    path('transfer/', transfer_funds, name='transfer_funds'),
]
