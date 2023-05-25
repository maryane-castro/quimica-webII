from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_exp_pratico', views.new_exp_pratico, name='new_exp_pratico' ),
    path('del_exp_pratico', views.del_exp_pratico, name='del_exp_pratico'),

    path('new_exp_teorico', views.new_exp_teorico, name='new_exp_teorico'),
    path('del_exp_teorico', views.del_exp_teorico, name='del_exp_teorico'),

]