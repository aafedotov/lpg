import csv
import os
from django.core.management.base import BaseCommand
from gaz.lpg.models import Lpg


class Command(BaseCommand):
    help = 'Экспорт данных из Lpg в CSV-файл'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Путь к файлу для сохранения данных')

    def handle(self, *args, **options):
        file_path = options['file'] or 'export.csv'

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            headers = [field.name for field in Lpg._meta.fields]
            writer.writerow(headers)

            for obj in Lpg.objects.all():
                row = [getattr(obj, field) for field in headers]
                writer.writerow(row)

        self.stdout.write(self.style.SUCCESS(f'Данные экспортированы в {file_path}'))
