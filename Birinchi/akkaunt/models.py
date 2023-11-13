from django.db import models

JINS = [
    ("Erkak", "Erkak"),
    ("Ayol", "Ayol"),
]


class Kontakt(models.Model):
    ism = models.CharField(max_length=30, unique=True)
    yosh = models.PositiveSmallIntegerField()
    talaba = models.BooleanField(default=True)
    sana = models.DateField(verbose_name="Ro'yhatdan o'tgan sanasi", auto_now_add=True)
    rasm = models.FileField()
    tel = models.CharField(max_length=15)
    jins = models.CharField(max_length=6, blank=True, choices=JINS)

    def __str__(self):  # doim string qaytarishi kerak
        return f"{self.ism} --> {self.tel}"


class Universitet(models.Model):
    nom = models.CharField(max_length=30)
    sana = models.DateField()
    talaba_soni = models.PositiveIntegerField()
    sayt = models.URLField()
    yillik = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.nom} --> {self.sayt}"


class Xodim(models.Model):
    ism = models.CharField(max_length=30)
    kasb = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    oylik = models.PositiveIntegerField(verbose_name="Oylik maosh ... $ da ")

    def __str__(self):
        return f"{self.ism} --> {self.kasb}"


class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    yosh = models.PositiveSmallIntegerField()
    jins = models.CharField(max_length=6, blank=True, choices=JINS)

    def __str__(self):
        return f"{self.ism} --> {self.email}"


class Foydalanuvchi(models.Model):
    username = models.CharField(max_length=30)
    rasm = models.FileField(blank=True, null=True)
    talaba = models.OneToOneField(Talaba, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} --> {self.talaba} "


class Nazoratchi(models.Model):
    ism = models.CharField(max_length=30)
    kasb = models.CharField(max_length=30, blank=True)
    yosh = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.ism


class Imtihon(models.Model):
    nazoratchi = models.ForeignKey(Nazoratchi, on_delete=models.CASCADE)
    talabalar = models.ManyToManyField(Talaba)
    manzil = models.CharField(max_length=100, null=True)
    sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nazoratchi}"


class Nashriyot(models.Model):
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} --> {self.manzil}"


class Kitob(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveIntegerField(verbose_name="Narxi ... so`m")
    kelgan_sana = models.DateField(blank=True, null=True)
    nashriyoti = models.ForeignKey(Nashriyot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} --> {self.nashriyoti}"


class Sotuvchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.ism} --> {self.tel}"


class Sotuv(models.Model):
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
    sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.kitob} --> {self.sotuvchi} --> {self.sana}"