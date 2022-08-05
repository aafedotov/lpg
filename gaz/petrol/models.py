from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Maintenance(models.Model):
    """Хранение отсечек ТО."""
    car = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='maintenances',
        verbose_name='Автомобиль',
        to_field='username',
    )
    next_mileage = models.FloatField(verbose_name='Следущее ТО (одометр)')


class Petrol(models.Model):
    """Описание модели для регистрации бензиновых запровок."""
    car = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='petrols',
        verbose_name='Автомобиль',
    )
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    volume = models.FloatField()
    cost = models.FloatField()
    odometer = models.FloatField()
    consumption = models.FloatField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date.date())
