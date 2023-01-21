from django.urls import path
from . import views     #'.' - из этой же папки импортируем метод views

from datetime import datetime

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import forms


urlpatterns = [
    path('', views.hello, name='home'),  # , name = 'home'
    # path('12', views.hello, name='home1'),
    path('addkl', views.addkl, name='addkl'),
    path('addu4', views.addu4, name='addu4'),
    path('addu41', views.addu41, name='addu41'),
    path('begin', views.begin, name='begin'),
    # path('dayend', views.dayend, name='dayend'),
    # path('instr', views.instr, name='instr'),
    # path('itog', views.itog, name='itog'),
    # path('itoglv', views.itoglv, name='itoglv'),
    # path('list1', views.list1, name='list1'),
    # path('list2', views.list2, name='list2'),
    # path('list3', views.list3, name='list3'),
    # path('list4', views.list4, name='list4'),
    # path('list5', views.list5, name='list5'),
    # path('list6', views.list6, name='list6'),
    # path('progress', views.progress, name='progress'),
    # path('level2', views.level2, name='level2'),
    # path('level3', views.level3, name='level3'),
    # path('level4', views.level4, name='level4'),
    # path('level5', views.level5, name='level5'),
    path('regist', views.regist, name='regist'),
    # path('reset', views.reset, name='reset'),
    # path('topday', views.topday, name='topday'),
    # path('toptab', views.toptab, name='toptab'),
    # path('toplvl', views.toplvl, name='toplvl'),
    # path('topglob', views.topglob, name='topglob'),
    # path('setcookie', views.setcookie, name='setcookie'),

    path('login/',
         LoginView.as_view
             (
             template_name='jsprob/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
