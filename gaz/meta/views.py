import base64
import json
import datetime as dt
import requests

from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from pathlib import Path

from .forms import MemoryForm

BASE_DIR = Path(__file__).parent
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDliZTJFZGY1NTBGMDEwZDQ1MzYxMWQwNDMxN0Q3MTU1RUU2NjQ2MTQiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NTc1MzU5MzU0OTcsIm5hbWUiOiJtZXRhbWVtb3J5In0.h3xx_IsIF-VqnOP0H0hVCoJ-kdN8m0MONOkxKRrSpdg'



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
        graves_dir = BASE_DIR / 'graves'
        graves_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'{obj_dict["name"]}_{now_formatted}.txt'
        with open(graves_dir / file_name, "w") as text_file:
            text_file.write(hex_hash)
        obj.save()
        multipart_form_data = {
            'file': (file_name, open(graves_dir / file_name, 'rb'), 'text/plain')
        }

        headers = {'Authorization': f'Bearer {TOKEN}'}

        response = requests.post('https://api.web3.storage/upload',
                                 files=multipart_form_data, headers=headers,
                                 verify=False)
        response_dict = json.loads(response.text)
        context = {'api_response': response_dict.get('cid')}
        return render(request, 'meta/success.html', context=context)
    template = 'meta/index.html'
    context = {'form': form}
    return render(request, template, context)
