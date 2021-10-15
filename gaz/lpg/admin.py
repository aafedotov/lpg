from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import url
import os
from .models import Lpg, File
from lpg.parsers import xlsx_lpg_parser as parser

from django.shortcuts import render
from django.conf import settings


class LpgAdmin(admin.ModelAdmin):

    list_display = ('date', 'price', 'mileage', 'benz_price',)

    change_list_template = "admin/model_change_list.html"
    def get_urls(self):
        urls = super(GroupAdmin, self).get_urls()
        custom_urls = [
                url('^import/$', self.process_import, name='process_import'),
                ]
        return custom_urls + urls

    def process_import(self, request):
        to_import = {}
        count = 0
        upload_file = File.objects.order_by('-pk')[0].filename()
        to_import = parser.XLSXLpgParser(upload_file)
        for i in range(98):
            date = to_import['date'][i]
            price = to_import['price'][i]
            volume = to_import['volume'][i]
            benz_price = to_import['benz_price'][i]
            cost = to_import['cost'][i]
            mileage = to_import['mileage'][i]
            mileage_total = to_import['mileage_total'][i]
            consump = to_import['consump'][i]
            saving = to_import['saving'][i]
            item = Lpg(date=date, price=price, volume=volume, benz_price=benz_price, cost=cost, mileage=mileage, mileage_total=mileage_total, consump=consump, saving=saving)
            item.save()
            count+=1
        self.message_user(request, f"Данные добавлены в базу. Количество новых записей: {count}")
        return HttpResponseRedirect("../")


admin.site.register(File)
admin.site.register(Lpg, LpgAdmin)
