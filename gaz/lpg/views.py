from django.shortcuts import render, redirect
import datetime
from .models import Lpg

def lpg_view(request):
    if request.user.username != 'faa':
        return redirect('/auth/login/')
    template = 'lpg/lpg.html'
    context = {'status' : '',
            'is_lpg':True,}
    if request.method == 'POST':
        status = 'Данные успешно переданы на сервер!'
        now = datetime.datetime.now()
        date = now.strftime("%d.%m.%Y")
        pricelpg = request.POST['pricelpg']
        litres = request.POST['litres']
        mileage = request.POST['mileage']
        price95 = request.POST['price95']
        last_lpg = Lpg.objects.all().order_by('-date').first()
        f = Lpg()
        f.price = round(float(pricelpg), 2) 
        f.volume = round(float(litres), 2)
        f.benz_price = round(float(price95), 2)
        f.cost = round(float(pricelpg)*float(litres), 2)
        f.mileage = round(float(mileage), 2)
        f.mileage_total = round((last_lpg.mileage_total + float(mileage)), 2)
        f.consump = round((last_lpg.volume/float(mileage)*100), 2)
        f.saving = round((float(mileage)/100*11.5*last_lpg.benz_price-last_lpg.cost), 2)
        f.save()
        context = {'status' : status,
                   'is_lpg':True,
        }
    return render(request, template, context)


def lpg_summary(request):
    if request.user.username != 'faa':
        return redirect('/auth/login/')
    template = 'lpg/lpg_summary.html'
    lpgs = Lpg.objects.all()
    last_lpg = lpgs.last()
    first_lpg = lpgs.first()
    total_saving = 0
    total_volume = 0
    total_cost = 0
    total_consump = 0
    count = 0
    for lpg in lpgs:
        count += 1
        total_saving += lpg.saving
        total_volume += lpg.volume
        total_cost += lpg.cost
        total_consump += lpg.consump
    total_consump = round((total_consump / count), 2)
    total_volume = round(total_volume, 2)
    total_cost = round(total_cost, 2)
    total_saving = round(total_saving, 2)
    total_days = datetime.date.today() - last_lpg.date.date()
    total_days = total_days.days
    total_mileage = int(first_lpg.mileage_total)
    context = {
            'total_saving': total_saving,
            'total_volume': total_volume,
            'total_cost': total_cost,
            'total_consump': total_consump,
            'total_days': total_days,
            'total_mileage': total_mileage,
            'lpg': lpgs,
            'is_lpg':True,
            }
    return render(request, template, context)