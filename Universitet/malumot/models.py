from django.db import models

JINS = [
    ("Erkak", "Erkak"),
    ("Ayol", "Ayol"),
]

DARAJA = [
    ("Bakalavr", "Bakalavr"),
    ("Magistr", "Magistr"),
    ("Professor", "Professor"),

]


class Yonalish(models.Model):
    nom = models.CharField(max_length=50)
    aktiv = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom}"


class Fan(models.Model):
    nom = models.CharField(max_length=50)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} --> {self.yonalish}"


class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=6, blank=True, choices=JINS)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=15, blank=True, choices=DARAJA)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism} --> {self.fan}"
