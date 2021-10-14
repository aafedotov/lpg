from django.shortcuts import render, redirect
import datetime

def lpg_view(request):
    if request.user.username != 'faa':
        return redirect('/auth/login/')
    template = 'lpg/lpg.html'
    status = ''
    context = {'status' : '',
            'pricelpg' : '',
            'litres' : '',
            'mileage' : '',
            'price95' : ''}
    if request.method == 'POST':
        status = 'Данные успешно переданы на сервер!'
        now = datetime.datetime.now()
        date = now.strftime("%d.%m.%Y")
        pricelpg = request.POST['pricelpg']
        litres = request.POST['litres']
        mileage = request.POST['mileage']
        price95 = request.POST['price95']
        f = open('bd.txt', 'a')
        f.write(f'{date}  {pricelpg}  {litres}  {mileage}  {price95} \n')
        f.close()
        context = {'status' : status}

    return render(request, template, context)
