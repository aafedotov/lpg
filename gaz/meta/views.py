import base64
import datetime as dt
import json
import os
from pathlib import Path

import requests
from django.shortcuts import render

from .forms import MemoryForm

BASE_DIR = Path(__file__).parent

TOKEN = os.getenv('WEB3_TOKEN')
API_URL = 'https://api.web3.storage/upload'


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

        multipart_form_data = {
            'file': (
                file_name,
                open(graves_dir / file_name, 'rb'),
                'text/plain'
            )
        }

        headers = {'Authorization': f'Bearer {TOKEN}'}

        response = requests.post(API_URL,
                                 files=multipart_form_data, headers=headers,
                                 verify=False)
        response_dict = json.loads(response.text)
        cid = response_dict.get('cid')
        obj.cid = cid
        obj.save()
        context = {'api_response': cid}
        return render(request, 'meta/success.html', context=context)

    template = 'meta/index.html'
    context = {'form': form}
    return render(request, template, context)
