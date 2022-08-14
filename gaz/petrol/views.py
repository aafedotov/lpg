from django.shortcuts import render, redirect, reverse
from django.db.models import Sum, Avg

from .models import Petrol, Maintenance


def petrol_success(request):
    """View-функция успешное добавление данных о заправке."""
    template = 'petrol/success.html'
    return render(request, template)


def petrol_view(request):
    """View-функция регистрации заправки бензином."""
    if request.user.username not in ('faa', 'Patriot'):
        return redirect('/auth/login/')
    template = 'petrol/petrol.html'
    maintenance = Maintenance.objects.filter(car=request.user).first()
    last_petrol = Petrol.objects.filter(car=request.user).order_by('-date').first()
    if last_petrol:
        maintenance = maintenance.next_mileage - last_petrol.odometer
    else:
        maintenance = maintenance.next_mileage
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
        new_petrol.car = request.user
        new_petrol.price = round(float(price), 2)
        new_petrol.volume = round(float(volume), 2)
        new_petrol.cost = round(float(price) * float(volume), 2)
        new_petrol.odometer = round(float(odometer), 2)
        if last_petrol:
            mileage = float(odometer) - last_petrol.odometer
            new_petrol.consumption = round((last_petrol.volume / float(mileage) * 100), 2)
        else:
            new_petrol.consumption = 0
        new_petrol.save()
        return redirect(reverse('petrol:success'))
    return render(request, template, context)


def petrol_summary(request):
    """View-функция для просмотра статистики затрат на бензин."""
    if request.user.username not in ('faa', 'Patriot'):
        return redirect('/auth/login/')
    template = 'petrol/petrol_summary.html'
    car = request.user.username
    petrols = Petrol.objects.filter(car=request.user)
    maintenance = Maintenance.objects.filter(car=request.user).first()
    if not petrols:
        context = {
            'car': car,
            'maintenance': maintenance.next_mileage,
        }
        return render(request, template, context)
    last_petrol = petrols.order_by('-date').first()
    first_petrol = petrols.order_by('-date').last()
    total_mileage = last_petrol.odometer - first_petrol.odometer
    if total_mileage == 0:
        total_mileage = last_petrol.odometer
    maintenance = maintenance.next_mileage - last_petrol.odometer
    total_odometer = last_petrol.odometer
    total_volume = petrols.aggregate(Sum('volume')).get('volume__sum')
    total_cost = petrols.aggregate(Sum('cost')).get('cost__sum')
    total_cost_per_km = round((total_cost - last_petrol.cost) / total_mileage, 2)
    total_consump = petrols.aggregate(Avg('consumption')).get('consumption__avg')
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
