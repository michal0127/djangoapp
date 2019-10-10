from django.db import models


class Miasto(models.Model):

    nazwa = models.CharField(verbose_name='miasto', max_length=30, help_text='Nazwa Miasta')
    kod = models.CharField(verbose_name='kod', max_length=8, help_text='Kod Pocztowy')


class Uczelnia(models.Model):

    uczelnia = models.CharField(verbose_name='uczelnia', max_length=50, help_text='Nazwa Uczelni')


class Student(models.Model):

    imie = models.CharField(verbose_name='imie', max_length=30)
    nazwisko = models.CharField(verbose_name='nazwisko', max_length=30)
    miasto = models.ForeignKey(Miasto, on_delete=models.SET_NULL, null=True)
    uczelnia = models.ForeignKey(Uczelnia, on_delete=models.SET_NULL, null=True)
    rok = models.CharField(verbose_name='rok studiów', max_length=3)
    dochod = models.DecimalField(max_digits=6, decimal_places=2)

