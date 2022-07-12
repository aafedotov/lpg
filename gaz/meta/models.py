from django.db import models


class Memory(models.Model):
    """Класс, описывающий поля для формирования блока памяти."""

    name = models.CharField(max_length=100)
    dob = models.DateField()
    dod = models.DateField()
    bio = models.TextField(blank=True)
    portrait = models.ImageField(upload_to='portraits/', null=True, blank=True)
    hex_hash = models.TextField(default='')
    cid = models.TextField(default='')

    def __str__(self):
        return self.name
