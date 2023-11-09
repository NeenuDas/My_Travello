from. import  views
from django.urls import path

urlpatterns = [

    path('form',views.form,name='form'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
