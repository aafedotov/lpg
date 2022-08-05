from django.shortcuts import render, redirect, reverse
import datetime
from .models import Lpg

import requests
from bs4 import BeautifulSoup


def get_benz_price():
    """Парсим текущую цену бензина."""
    url = 'https://fuelprice.ru/azs16708'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    prices = soup.find_all('span', class_='text-success font-weight-bold')
    dates = soup.find_all('small', class_='text-')
    price = {'price': prices[1].text, 'date': dates[0].text}
    return price


def lpg_success(request):
    """View-функция успешное добавление данных о заправке."""
    template = 'lpg/success.html'
    return render(request, template)


def lpg_view(request):
    """View-функция регистрации заправки газом."""
    if request.user.username != 'faa':
        return redirect('/auth/login/')
    template = 'lpg/lpg.html'
    price = get_benz_price()
    last_lpg = Lpg.objects.all().order_by('-date').first()
    maintenance = last_lpg.maintenance
    lpg_maintenance = last_lpg.lpg_maintenance
    car = request.user.username
    context = {'status': '',
               'is_lpg': True,
               'price': price['price'],
               'date': price['date'],
               'maintenance': maintenance,
               'lpg_maintenance': lpg_maintenance,
               'car': car,
               }
    if request.method == 'POST':
        now = datetime.datetime.now()
        pricelpg = request.POST['pricelpg']
        litres = request.POST['litres']
        mileage = request.POST['mileage']
        price95 = request.POST['price95']
        f = Lpg()
        f.date = now
        f.price = round(float(pricelpg), 2)
        f.volume = round(float(litres), 2)
        f.benz_price = round(float(price95), 2)
        f.cost = round(float(pricelpg) * float(litres), 2)
        f.mileage = round(float(mileage), 2)
        f.mileage_total = round((last_lpg.mileage_total + float(mileage)), 2)
        f.consump = round((last_lpg.volume / float(mileage) * 100), 2)
        f.saving = round((float(
            mileage) / 100 * 11.5 * last_lpg.benz_price - last_lpg.cost), 2)
        f.maintenance = last_lpg.maintenance - int(mileage)
        f.lpg_maintenance = last_lpg.lpg_maintenance - int(mileage)
        f.save()
        return redirect(reverse('lpg:success'))
    return render(request, template, context)


def lpg_summary(request):
    """View-функция для просмотра статистики."""
    if request.user.username not in ('faa', 'Patriot'):
        return redirect('/auth/login/')
    template = 'lpg/lpg_summary.html'
    lpgs = Lpg.objects.filter(car=request.user)
    last_lpg = lpgs.last()
    first_lpg = lpgs.first()
    total_saving = 0
    total_volume = 0
    total_cost = 0
    total_consump = 0
    count = 0
    chart_data = []
    chart_mileage = {}
    chart_cost = {}
    for lpg in lpgs:
        data = []
        date_str = f'{lpg.date.date().year}, {lpg.date.date().month}'
        if date_str not in chart_mileage:
            chart_mileage[date_str] = 0
            chart_cost[date_str] = 0
        chart_mileage[date_str] += lpg.mileage
        chart_cost[date_str] += lpg.cost
        data.append(date_str)
        data.append(lpg.price)
        data.append(lpg.benz_price)
        chart_data.append(data)
        count += 1
        total_saving += lpg.saving
        total_volume += lpg.volume
        total_cost += lpg.cost
        total_consump += lpg.consump
    chart_data.reverse()
    chart_mileage = list(map(list, chart_mileage.items()))
    chart_mileage.reverse()
    chart_cost = list(map(list, chart_cost.items()))
    chart_cost.reverse()
    total_consump = round((total_consump / count), 2)
    total_volume = round(total_volume, 2)
    total_cost = round(total_cost, 2)
    total_saving = round(total_saving, 2)
    total_days = datetime.date.today() - last_lpg.date.date()
    total_days = total_days.days
    total_mileage = int(first_lpg.mileage_total)
    maintenance = first_lpg.maintenance
    lpg_maintenance = first_lpg.lpg_maintenance
    car = request.user.username
    context = {
        'total_saving': total_saving,
        'total_volume': total_volume,
        'total_cost': total_cost,
        'total_consump': total_consump,
        'total_days': total_days,
        'total_mileage': total_mileage,
        'lpg': lpgs,
        'is_lpg': True,
        'chart_data': chart_data,
        'chart_mileage': chart_mileage,
        'chart_cost': chart_cost,
        'lpg_maintenance': lpg_maintenance,
        'maintenance': maintenance,
        'car': car,
    }
    return render(request, template, context)
