from django.db import models

# Create your models here.
from django.utils import timezone
class MiniURL(models.Model):
    url_longue = models.URLField(unique=True)
    code_raccourci = models.CharField(max_length=42)
    date_raccourci = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    pseudo_createur = models.CharField(max_length=42)
    nombre_acces = models.IntegerField(default=0)

    class Meta:
        ordering = ['date_raccourci']

    def __str__(self):
        return self.url_longue