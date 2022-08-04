from django.shortcuts import render, redirect, reverse
from django.db.models import Sum

from .forms import STOForm
from .models import STO


def sto_success(request):
    template = 'sto/success.html'
    return render(request, template)


def sto_view(request):
    """View-функция для формы чек-ина ТО."""
    if request.user.username not in ('faa', 'Patriot'):
        return redirect('/auth/login/')
    is_sto = True
    form = STOForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('sto:success'))
    template = 'sto/sto.html'
    context = {'form': form, 'is_sto': is_sto}
    return render(request, template, context)


def sto_summary(request):
    """View-функция для саммари по ТО."""
    if request.user.username not in ('faa', 'Patriot'):
        return redirect('/auth/login/')
    template = 'sto/sto_summary.html'
    stos = STO.objects.filter(car=request.user)
    total = stos.aggregate(Sum('price')).get('price__sum')
    car = request.user.username
    context = {'stos': stos, 'total': total, 'car': car}
    return render(request, template, context)
