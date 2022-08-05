from django.shortcuts import render, redirect, reverse
from django.db.models import Sum, Avg

from .models import Petrol


def petrol_success(request):
    """View-функция успешное добавление данных о заправке."""
    template = 'petrol/success.html'
    return render(request, template)


def petrol_view(request):
    """View-функция регистрации заправки бензином."""
    if request.user.username not in ('faa', 'Patriot'):
        return redirect('/auth/login/')
    template = 'petrol/petrol.html'
    last_petrol = Petrol.objects.all().order_by('-date').first()
    maintenance = last_petrol.maintenance
    car = request.user.username
    context = {
        'is_petrol': True,
        'maintenance': maintenance,
        'car': car,
    }
    if request.method == 'POST':
        price = request.POST['price']
        volume = request.POST['volume']
        odometer = request.POST['odometer']
        new_petrol = Petrol()
        new_petrol.price = round(float(price), 2)
        new_petrol.volume = round(float(volume), 2)
        new_petrol.cost = round(float(price) * float(volume), 2)
        new_petrol.odometer = round(float(odometer), 2)
        if last_petrol:
            mileage = odometer - last_petrol.odometer
            new_petrol.consumption = round((last_petrol.volume / float(mileage) * 100), 2)
            new_petrol.maintenance = last_petrol.maintenance - mileage
        else:
            new_petrol.consumption = 0
            new_petrol.maintenance = 0
        new_petrol.save()
        return redirect(reverse('petrol:success'))
    return render(request, template, context)


def petrol_summary(request):
    """View-функция для просмотра статистики затрат на бензин."""
    if request.user.username not in ('faa', 'Patriot'):
        return redirect('/auth/login/')
    template = 'petrol/petrol_summary.html'
    petrols = Petrol.objects.filter(car=request.user)
    last_petrol = petrols.order_by('-date').first()
    first_petrol = petrols.order_by('-date').last()
    total_mileage = last_petrol.odometer - first_petrol.odometer
    maintenance = last_petrol.maintenance
    total_odometer = last_petrol.odometer
    total_volume = petrols.aggregate(Sum('volume'))
    total_cost = petrols.aggregate(Sum('cost'))
    total_cost_per_km = round(total_cost / total_mileage, 2)
    total_consump = petrols.aggregate(Avg('consumption'))
    car = request.user.username
    context = {
        'total_volume': total_volume,
        'total_cost': total_cost,
        'total_consump': total_consump,
        'total_mileage': total_odometer,
        'total_cost_per_km': total_cost_per_km,
        'petrols': petrols,
        'is_petrol': True,
        'maintenance': maintenance,
        'car': car,
    }
    return render(request, template, context)
