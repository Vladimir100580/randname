from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import DataKlass
from django.contrib.auth import authenticate, login


def hello(request):
    answer = request.GET
    user_id = request.user.username
    try:
        po = request.session['klas_use']
    except:
        request.session['phdlyavvoda'] = ''
        request.session['klas_use'] = ''
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
    if 'addu44' in answer:
        request.session['wayrnd'] = '3'
        return redirect('addu4')
    return render(request, 'jsprob/priv.html', {'nm': nm, 'fl': fl, 'fl0': fl0, 'f': f})


def regist(request):
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
    klData = DataKlass.objects.filter(log=user_id, klass=kl).values_list('fios', 'vyhods', 'balls','res2')
    nms = klData[0][0].split('$}%*№')
    vyhs = klData[0][1].split('$}%*№')
    bals = klData[0][2].split('$}%*№')
    totv = request.session['totalvyhods'] = int(klData[0][3])
    pvyh = StringToArrayIntegers(request.session['phdlyavvoda']).arr
    i = 0
    masv = []
    vrs = 0
    try:
        for ii in vyhs:
            if i+1 not in pvyh:
                k = 3 ** (totv - int(ii))
                if k < 2: k = 0
                vrs += k
            i += 1
    except:
        return redirect('addu41')
    i = 0
    if vrs != 0:
        for ii in vyhs:
            if i + 1 not in pvyh:
                k = 3 ** (totv - int(ii))
                if k < 2: k = 0
                vspom = int(1000*k/vrs + 0.5)/10
                if vspom==int(vspom): vspom=int(vspom)
                masv.append(str(vspom))
            else:
                masv.append('-')
            i += 1
    else:
        for ii in vyhs:
            if i + 1 not in pvyh:
                masv.append("0")
            else:
                masv.append("-")
            i += 1
    datnvb = []
    for i in range(len(nms)):
        datnvb.append([str(i % 3), str(i + 1) + ') ' + nms[i], vyhs[i], bals[i], masv[i] + '%'])
    if 'gogo' in answer:
        st = answer.__getitem__('iskl').strip()
        if st != '':
            arisk = StringToArrayIntegers(st).arr
        else: arisk = []
        for i in arisk:
            if i not in range(1, len(nms) + 1):
                return render(request, 'jsprob/nonom.html', {'i': str(i)})
        nms1 = []
        vyhrnd = []
        for i in range(0, len(nms)):
            if (i+1) not in arisk:
                nms1.append(nms[i])
                vyhrnd.append(int(float(vyhs[i])))
        if request.session['phdlyavvoda'] == st:
            request.session['rndpernamord'] = [[ord(i) for i in n] for n in nms1]
            request.session['rndpernamord1'] = [n for n in nms1]
            request.session['rndpervyh'] = vyhrnd
            return redirect('start')
        else:
            request.session['phdlyavvoda'] = st
            return redirect('begin')
    return render(request, 'jsprob/begin.html', {'nms': datnvb, 'ph': request.session['phdlyavvoda'], 'kl': kl})


def start(request):
    data = {
        'nam': request.session['rndpernamord'],
        'vyh': request.session['rndpervyh'],
        'vv': request.session['totalvyhods'],
    }
    answer = request.GET
    if 'kb' in answer:
        b = float(answer.__getitem__('kb'))
        req = request.COOKIES.get('pndnameu4').split('$')
        uch = ''.join(chr(int(float(i))) for i in req)
        user_id = request.user.username
        if (user_id == ''): return redirect('home')
        kl = request.session['klas_use']
        kar = DataKlass.objects.get(log=user_id, klass=kl)
        nms = kar.fios.split('$}%*№')
        vyhs = [int(float(i)) for i in kar.vyhods.split('$}%*№')]
        bals = [int(float(i)) for i in kar.balls.split('$}%*№')]
        p = nms.index(uch)
        vyhs[p] = vyhs[p] + 1
        bals[p] = bals[p] + b
        p = request.session['rndpernamord1'].index(uch)
        vsel = request.session['rndpervyh']
        vsel[p] += 1
        request.session['rndpervyh'] = vsel
        vyhs = [str(int(i)) for i in vyhs]
        bals = [str(int(i)) for i in bals]
        kar.vyhods = '$}%*№'.join(vyhs)
        kar.balls = '$}%*№'.join(bals)
        kar.save()
        return redirect('start')
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
        kl = answer.__getitem__('kl').replace(' ', '_')
        vv = int(answer.__getitem__('vv'))
        if kl == '': return redirect('addkl')
        if DataKlass.objects.filter(klass=kl, log=user_id).exists():
            return render(request, 'jsprob/ujusekl.html')
        DataKlass(log=user_id, klass=kl, fios='', vyhods='', balls='', res2=vv).save()
        return redirect('home')
    return render(request, 'jsprob/addkl.html', {'kls': st})


def addu4(request):
    answer = request.GET
    user_id = request.user.username
    if (user_id == ''): return redirect('home')
    kls = DataKlass.objects.order_by('klass').filter(log=user_id).values_list('klass')
    if len(kls) == 1:
        request.session['klas_use'] = kls[0][0]
        if request.session['wayrnd'] == '1': return redirect('begin')
        if request.session['wayrnd'] == '2': return redirect('addu41')
        if request.session['wayrnd'] == '3': return redirect('addu44')
        if request.session['wayrnd'] == '4': return redirect('copylist')
    klasMas = [i[0] for i in kls]

    if 'intlg' in answer:
        kl = answer.__getitem__('nomm')
        if request.session['klas_use'] != kl:
            request.session['klas_use'] = kl
            request.session['phdlyavvoda'] = ''
        if request.session['wayrnd'] == '1': return redirect('begin')
        if request.session['wayrnd'] == '2': return redirect('addu41')
        if request.session['wayrnd'] == '3': return redirect('addu44')
        if request.session['wayrnd'] == '4': return redirect('copylist')
    return render(request, 'jsprob/addu4.html', {'klasss': klasMas, 'fl': request.session['wayrnd']})


def addu41(request):
    answer = request.GET
    f = 0
    fl = 0
    user_id = request.user.username
    if (user_id == ''): return redirect('home')
    kl = request.session['klas_use']
    klData = DataKlass.objects.filter(log=user_id, klass=kl).values_list('fios', 'vyhods', 'balls')
    nms = klData[0][0].split('$}%*№')
    vyhs = klData[0][1].split('$}%*№')
    bals = klData[0][2].split('$}%*№')
    datnvb = []
    for i in range(len(nms)): datnvb.append([str(i % 3), str(i + 1) + ') ' + nms[i], vyhs[i], bals[i]])
    if len(datnvb) <= 2: fl = 1
    if 'copy' in answer:
        request.session['wayrnd'] = '4'
        request.session['klas_use_p'] = request.session['klas_use']
        return redirect('addu4')
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
    return render(request, 'jsprob/addu41.html', {'nms': datnvb, 'fl': fl, 'kl': kl})


def addu44(request):      # изменение количества выходов
    answer = request.GET
    user_id = request.user.username
    if (user_id == ''): return redirect('home')
    kl = request.session['klas_use']
    kls = DataKlass.objects.get(log=user_id, klass=kl)
    if 'klvyh' in answer:
        kls.res2 = int(answer.__getitem__('vv'))
        kls.save(update_fields=['res2'])
        return redirect('addu44')
    return render(request, 'jsprob/izmvyh.html', {'kl': kl, 'vyh': kls.res2})


def copylist(request):
    user_id = request.user.username
    if (user_id == ''): return redirect('home')
    kl = request.session['klas_use']
    klData = DataKlass.objects.filter(log=user_id, klass=kl).values_list('fios', 'vyhods', 'balls')
    nms = klData[0][0].split('$}%*№')
    vyhs = '$}%*№'.join(['0' for _ in range(len(nms))])
    bals = '$}%*№'.join(['0' for _ in range(len(nms))])
    kar = DataKlass.objects.get(log=user_id, klass=request.session['klas_use_p'])
    kar.fios = '$}%*№'.join(nms)
    kar.vyhods = vyhs
    kar.balls = bals
    kar.save()
    request.session['klas_use'] = request.session['klas_use_p']
    return redirect('addu41')


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