from django.db import models
from django.contrib.auth import get_user_model

import os

User = get_user_model()


class Lpg(models.Model):
    """Описание модели для регистрации газовых запровок."""
    car = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lpgs',
        verbose_name='Автомобиль',
        to_field='username',
        default='faa',
    )
    date = models.DateTimeField()
    price = models.FloatField()
    volume = models.FloatField()
    benz_price = models.FloatField()
    cost = models.FloatField()
    mileage = models.FloatField()
    mileage_total = models.FloatField()
    consump = models.FloatField()
    saving = models.FloatField()
    maintenance = models.IntegerField(blank=True, default=0)
    lpg_maintenance = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return str(self.date.date())


class File(models.Model):
    
    file = models.FileField(upload_to='')

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.filename()