from django.db import models
import os
  
class Lpg(models.Model):

    date = models.DateTimeField()
    price = models.FloatField()
    volume = models.FloatField()
    benz_price = models.FloatField()
    cost = models.FloatField()
    mileage = models.FloatField()
    mileage_total = models.FloatField()
    consump = models.FloatField()
    saving = models.FloatField()

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