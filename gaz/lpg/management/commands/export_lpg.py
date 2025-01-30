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
        totals_file_path = 'export_total.csv'
        mileage_file_path = 'export_mileage.csv'
        cost_file_path = 'export_cost.csv'
        price_file_path = 'export_price.csv'

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

        context_mileage = context['chart_mileage']

        context_cost = context['chart_cost']

        context_price = context['chart_data']

        with open(totals_file_path, mode='w', newline='', encoding='utf-8') as file:

            writer = csv.writer(file)

            writer.writerow([key for key in context_totals])
            writer.writerow([context_totals[key] for key in context_totals])

        with open(mileage_file_path, mode='w', newline='', encoding='utf-8') as file:

            writer = csv.writer(file)

            writer.writerow(['month', 'mileage'])
            for row in context_mileage:
                writer.writerow([item for item in row])

        with open(cost_file_path, mode='w', newline='', encoding='utf-8') as file:

            writer = csv.writer(file)

            writer.writerow(['month', 'cost'])
            for row in context_cost:
                writer.writerow([item for item in row])

        with open(price_file_path, mode='w', newline='', encoding='utf-8') as file:

            writer = csv.writer(file)

            writer.writerow(['date', 'lpg', 'petrol'])
            for row in context_price:
                writer.writerow([item for item in row])


        self.stdout.write(self.style.SUCCESS(f'Данные экспортированы в {mileage_file_path}'))
        self.stdout.write(self.style.SUCCESS(f'Данные экспортированы в {totals_file_path}'))
        self.stdout.write(self.style.SUCCESS(f'Данные экспортированы в {cost_file_path}'))
        self.stdout.write(self.style.SUCCESS(f'Данные экспортированы в {price_file_path}'))
