from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('dash', views.dash, name='dash'),


    path('new_exp_pratico', views.new_exp_pratico, name='new_exp_pratico' ),
    path('new_exp_teorico', views.new_exp_teorico, name='new_exp_teorico'), #ko


    
    path('del_exp_teorico/<int:pk>', del_exp_teorico, name='del_exp_teorico'),

]