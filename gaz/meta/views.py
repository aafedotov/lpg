import base64
import json

from django.shortcuts import render, redirect, reverse


from .forms import MemoryForm


def meta_success(request):
    template = 'meta/success.html'
    return render(request, template)


def index(request):
    """View-функция для формы заявки на формирование блока памяти."""

    form = MemoryForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        encoded_portrait = base64.b64encode(obj.portrait.read())
        obj_dict = {
            'name': str(obj.name),
            'dob': str(obj.dob),
            'dod': str(obj.dod),
            'bio': str(obj.bio),
            'portrait': str(encoded_portrait)
        }

        obj_json = json.dumps(obj_dict)
        hex_hash = ''
        for char in obj_json:
            hex_hash += hex(ord(char))[2:]
        obj.hex_hash = hex_hash
        obj.save()

        return redirect(reverse('meta:success'))
    template = 'meta/index.html'
    context = {'form': form}
    return render(request, template, context)
