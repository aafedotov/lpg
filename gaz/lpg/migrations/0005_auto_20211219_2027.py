# Generated by Django 3.2.7 on 2021-12-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpg', '0004_alter_lpg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpg',
            name='lpg_maintenance',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='lpg',
            name='maintenance',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]