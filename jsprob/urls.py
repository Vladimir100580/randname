from django.urls import path
from . import views     #'.' - из этой же папки импортируем метод views
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from . import forms


urlpatterns = [
    path('', views.hello, name='home'),  # , name = 'home'
    path('addkl', views.addkl, name='addkl'),
    path('addu4', views.addu4, name='addu4'),
    path('addu41', views.addu41, name='addu41'),
    path('addu44', views.addu44, name='addu44'),
    path('begin', views.begin, name='begin'),
    path('start', views.start, name='start'),
    path('regist', views.regist, name='regist'),


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
