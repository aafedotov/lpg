import csv
import os
from django.core.management.base import BaseCommand
from lpg.models import Lpg
from lpg.views import get_summary_data



class Command(BaseCommand):
    help = 'Экспорт данных из Lpg в CSV-файл'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Путь к файлу для сохранения данных')

    def handle(self, *args, **options):
        totals_file_path = options['file'] or 'export_total.csv'
        context = get_summary_data('Patriot')
        context_totals = {
            'total_saving': context['total_saving'],
            'total_volume': context['total_volume'],
            'total_cost': context['total_cost'],
            'total_consump': context['total_consump'],
            'total_days': context['total_days'],
            'total_mileage': context['total_mileage'],
            'lpg_maintenance': context['lpg_maintenance'],
            'maintenance': context['maintenance'],
            'total_cost_per_km': context['total_cost_per_km']
        }

        with open(totals_file_path, mode='w', newline='', encoding='utf-8') as file:

            writer = csv.writer(file)

            writer.writerow([key for key in context_totals])
            writer.writerow([context_totals[key] for key in context_totals])

        self.stdout.write(self.style.SUCCESS(f'Данные экспортированы в {totals_file_path}'))
