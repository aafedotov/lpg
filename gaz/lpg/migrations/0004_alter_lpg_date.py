# Generated by Django 3.2.7 on 2021-10-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpg', '0003_alter_lpg_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpg',
            name='date',
            field=models.DateTimeField(),
        ),
    ]