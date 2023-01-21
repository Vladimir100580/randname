import time, datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from random import randint
from .models import DataKlass, Indexs
from django.contrib.auth import authenticate, login


def hello(request):
    answer = request.GET
    user_id = request.user.username
    fl0 = '0'
    if (user_id != ''):
        nm = request.user.first_name.split('$#$%')
        if len(nm) == 4: fl0 = '1'
        nm = ', ' + nm[1] + ' ' + nm[2]
        fl = 1
    else:
        nm = ''
        fl = 0

    f = 0
    if DataKlass.objects.filter(log=user_id).exists(): f = 1


    if 'reg' in answer:
        return redirect('regist')
    if 'intlg' in answer:

        lg = answer.__getitem__('lg')
        if len(lg) < 3: return redirect('home')
        if User.objects.filter(username=lg).exists():
            user = authenticate(request, username=lg, password='4591423')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'jsprob/nezar.html')
    return render(request, 'jsprob/priv.html', {'nm': nm, 'fl': fl, 'fl0': fl0, 'f': f})


def regist(request):
    # return redirect('logout')
    if request.method == 'GET':
        answer = request.GET
        if 'fam' in answer and 'name' in answer and 'lg' in answer:
            f = answer.__getitem__('fam').replace(' ', '').capitalize()
            n = answer.__getitem__('name').replace(' ', '').capitalize()
            if f == '' or n == '': return redirect('regist')
            k = answer.__getitem__('kl').replace(' ', '')
            lg = answer.__getitem__('lg')
            if len(f) < 2 or len(n) < 2 or len(f) > 25 or len(n) > 25 or len(k) > 25 or len(lg) > 40 or len(lg) < 3:
                return redirect('regist')
            if User.objects.filter(username=lg).exists():
                return render(request, 'jsprob/ujuse.html')
            else:
                user = User.objects.create_user(lg, '', '4591423', first_name=f + '$#$%' + n + '$#$%' + k)
                user.save()
                user = authenticate(request, username=lg, password='4591423')
                login(request, user)
                return render(request, 'jsprob/uspreg.html')
    return render(request, 'jsprob/registr.html')



def begin(request):
    print('Ку-ку')


def addkl(request):
    answer = request.GET
    user_id = request.user.username

    if (user_id == ''): return redirect('home')

    kls = DataKlass.objects.order_by('klass').filter(log=user_id).values_list('klass')
    st = ''
    if len(kls) > 0:
        st = 'Ваши классы: '
        for i in kls: st = st + i[0] + ', '
        st = st[:len(st) - 2] + '.'


    if 'kl' in answer:
        kl = answer.__getitem__('kl')
        if kl == '': return redirect('addkl')
        if DataKlass.objects.filter(klass=kl, log=user_id).exists():
            return render(request, 'jsprob/ujusekl.html')
        DataKlass(log=user_id, klass=kl).save()
        return redirect('addkl')

    return render(request, 'jsprob/addkl.html', {'kls': st})


def addu4(request):
    answer = request.GET
    user_id = request.user.username
    if (user_id == ''): return redirect('home')
    kls = DataKlass.objects.order_by('klass').filter(log=user_id).values_list('klass')
    if len(kls) == 1:
        request.session['klas_use'] = kls[0][0]
        return redirect('addu41')
    klasMas = [i[0] for i in kls]
    print('klasMas-', klasMas)


    if 'intlg' in answer:
        kl = answer.__getitem__('nomm')
        request.session['klas_use'] = kl
        return redirect('addu41')

    return render(request, 'jsprob/addu4.html', {'klasss': klasMas})


def addu41(request):
    print(1)