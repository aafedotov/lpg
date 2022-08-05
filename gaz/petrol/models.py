from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


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
    maintenance = models.FloatField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date.date())
