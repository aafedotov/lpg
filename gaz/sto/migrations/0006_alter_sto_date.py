# Generated by Django 3.2.7 on 2021-12-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sto', '0005_auto_20211227_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sto',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]