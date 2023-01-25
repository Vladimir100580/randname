from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import DataKlass
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
    if 'begin' in answer:
        request.session['wayrnd'] = '1'
        return redirect('addu4')
    if 'addu4' in answer:
        request.session['wayrnd'] = '2'
        return redirect('addu4')
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
    answer = request.GET
    user_id = request.user.username
    if (user_id == ''): return redirect('home')
    kl = request.session['klas_use']
    klData = DataKlass.objects.filter(log=user_id, klass=kl).values_list('fios', 'vyhods', 'balls')
    nms = klData[0][0].split('$}%*№')
    vyhs = klData[0][1].split('$}%*№')
    bals = klData[0][2].split('$}%*№')
    datnvb = []
    for i in range(len(nms)):
        datnvb.append([str(i % 3), str(i + 1) + ') ' + nms[i], vyhs[i], bals[i]])

    if 'gogo' in answer:
        st = answer.__getitem__('iskl').strip()
        if st != '':
            arisk = StringToArrayIntegers(st).arr
        else: arisk = []
        datnvb = []
        for i in arisk:
            if i not in range(1, len(nms) + 1):
                return render(request, 'jsprob/nonom.html', {'i': str(i)})
        k = 0
        for i in nms:
            if float(vyhs[k]) ** 2 >= 8 and k not in arisk:
                print('k', k, float(vyhs[k]) ** 2, arisk)
                arisk.append(k)
            k += 1

        nms1 = []
        vyhrnd = []
        for i in range(0, len(nms)):
            if (i+1) not in arisk:
                nms1.append(nms[i])
                vyhrnd.append(int(float(vyhs[i])))
                datnvb.append([str(i % 3), str(i + 1) + ') ' + nms[i], vyhs[i], i])

        request.session['rndpernamord'] = [[ord(i) for i in n] for n in nms1]
        request.session['rndpervyh'] = vyhrnd
        return redirect('start')

        return render(request, 'jsprob/start.html', {'nms': datnvb})

    return render(request, 'jsprob/begin.html', {'nms': datnvb})


def start(request):

    data = {
        'nam': request.session['rndpernamord'],
        'vyh': request.session['rndpervyh'],
    }
    answer = request.GET
    if 'kb' in answer:
        b = float(answer.__getitem__('kb'))
        u4 = request.COOKIES.get('pndnameu4')
        print('ball=', b, u4)
        user_id = request.user.username
        if (user_id == ''): return redirect('home')
        kl = request.session['klas_use']
        kar = DataKlass.objects.get(log=user_id, klass=kl)
        nms = kar.fios.split('$}%*№')
        vyhs = kar.vyhods.split('$}%*№')
        bals = kar.balls.split('$}%*№')
        p = nms.index(u4)
        vyhs[p] = str(int(float(vyhs[p])+1))
        bals[p] = str(int(float(bals[p]) + b))
        kar.vyhods = '$}%*№'.join(vyhs)
        kar.balls = '$}%*№'.join(bals)
        kar.save()
    if 'rep' in answer: return redirect('start')
    if 'klass' in answer: return redirect('begin')


    return render(request, 'jsprob/start.html', data)

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
        DataKlass(log=user_id, klass=kl, fios='', vyhods='', balls='').save()
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

    if 'intlg' in answer:
        kl = answer.__getitem__('nomm')
        request.session['klas_use'] = kl
        if request.session['wayrnd'] == '1': return redirect('begin')
        if request.session['wayrnd'] == '2': return redirect('addu41')
    return render(request, 'jsprob/addu4.html', {'klasss': klasMas})


def addu41(request):
    answer = request.GET
    f = 0
    user_id = request.user.username
    if (user_id == ''): return redirect('home')
    kl = request.session['klas_use']
    klData = DataKlass.objects.filter(log=user_id, klass=kl).values_list('fios', 'vyhods', 'balls')
    nms = klData[0][0].split('$}%*№')
    vyhs = klData[0][1].split('$}%*№')
    bals = klData[0][2].split('$}%*№')
    datnvb = []
    for i in range(len(nms)): datnvb.append([str(i % 3), str(i + 1) + ') ' + nms[i], vyhs[i], bals[i]])
    if 'intfi' in answer:
        fami = answer.__getitem__('famim').strip()
        if len(fami) < 3: return redirect('addu41')
        if DataKlass.objects.filter(log=user_id, klass=kl).exists() and fami in nms:
            return render(request, 'jsprob/ujusefi.html', {'fami': fami, 'kl': kl})
        if nms[0] == '':
            nms[0] = fami
            vyhs[0] = '0'
            bals[0] = '0'
        else:
            nms.append(fami)
            vyhs.append('0')
            bals.append('0')
        f = 1
    if 'delfi' in answer:
        fami = answer.__getitem__('famim').strip()
        if len(fami) < 3: return redirect('addu41')
        if fami not in nms:
            return render(request, 'jsprob/nofi.html', {'fami': fami, 'kl': kl})
        i = nms.index(fami)
        nms.pop(i)
        vyhs.pop(i)
        bals.pop(i)
        f = 1
    if f == 1:
        fl = 1
        while fl == 1:
            fl = 0
            for i in range(len(nms) - 1):
                if nms[i] > nms[i + 1]:
                    nms[i], nms[i + 1] = nms[i + 1], nms[i]
                    vyhs[i], vyhs[i + 1] = vyhs[i + 1], vyhs[i]
                    bals[i], bals[i + 1] = bals[i + 1], bals[i]
                    fl = 1
        kar = DataKlass.objects.get(log=user_id, klass=kl)
        kar.fios = '$}%*№'.join(nms)
        kar.vyhods = '$}%*№'.join(vyhs)
        kar.balls = '$}%*№'.join(bals)
        kar.save()
        return redirect('addu41')
    return render(request, 'jsprob/addu41.html', {'nms': datnvb})


class StringToArrayIntegers:
    def __init__(self, st):
        f = 0
        s = ''
        mas = []
        st = st + ' '
        for i in st:
            if i.isdigit() or i == '-':
                s += i
                f = 1
            else:
                if f == 1:
                    mas.append(int(float(s)))
                    s = ''
                    f = 0
        self.arr = mas