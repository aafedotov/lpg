# Generated by Django 3.2.7 on 2021-10-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpg',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]