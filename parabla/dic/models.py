from django.db import models


class Zdanie(models.Model):
    zdanie_zdanie=models.TextField(null=False)
    #zdanie_slowo=models.ForeignKey(Slowo, on_delete=models.CASCADE)

    def __str__(self):
        return self.zdanie_zdanie


class Slowo(models.Model):
    slowo_slowo=models.CharField(max_length=50)

    CZASOWNIK='Czas.'
    RZECZOWNIK='Rzecz.'
    PRZYMIOTNIK='Przym.'
    DROBNICA='Drob.'
    CZESCI_MOWY_CHOICES=(
        (CZASOWNIK,'Czasownik'),
        (RZECZOWNIK, 'Rzeczownik'),
        (PRZYMIOTNIK, 'Przymiotnik'),
        (DROBNICA, 'Drobnica')
    )
    slowo_czesc=models.CharField(max_length=20,
        choices=CZESCI_MOWY_CHOICES,
        default=DROBNICA,)
    slowo_zdanie=models.ForeignKey(Zdanie, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.slowo_slowo


# Create your models here.
