from django.shortcuts import render

def index(request):
    template = 'index/index.html'
    return render(request, template)