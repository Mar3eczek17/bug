from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Wiadomosc(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    tekst = models.CharField('treść wiadomości', max_length=250)
    created_date = models.DateTimeField('data publikacji')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = u'wiadomość'  # nazwa obiektu w języku polskim
        verbose_name_plural = u'wiadomości'  # nazwa obiektów w l.m.
        ordering = ['created_date']  # domyślne porządkowanie danych

    def __str__(self):
        return self.tekst
