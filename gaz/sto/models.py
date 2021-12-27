from django.db import models


class Group(models.Model):
    """Модель с типом обслуживания."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    """Перечень работ."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class STO(models.Model):
    """Модель с записями о прошедших ТО."""
    date = models.DateField()
    mileage = models.IntegerField()
    group = models.ForeignKey(
        Group,
        related_name='stos',
        default=1,
        on_delete=models.SET_DEFAULT,
        blank=False, null=False
    )
    actions = models.ManyToManyField(Action)
    price = models.IntegerField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date)
