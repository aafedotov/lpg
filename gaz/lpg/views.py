from django.shortcuts import render

def lpg_view(request):
    template = 'lpg/lpg.html'
    status = ''
    if request.method == 'POST':
        status = 'Данные успешно переданы на сервер!'
    context = {'status': status}
    return render(request, template, context)
