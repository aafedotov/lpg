from django.db import models

class Lpg(models.Model):

    lpg_date = models.DateTimeField()
    lpg_price = models.FloatField()
    lpg_volume = models.FloatField()
    benz_price = models.FloatField()
    lpg_cost = models.FloatField()
    lpg_mileage = models.FloatField()
    lpg_mileage_total = models.FloatField()
    lpg_consump = models.FloatField()
    lpg_saving = models.FloatField()
