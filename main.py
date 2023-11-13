# Kitob.objects.all().order_by("-sahifa").first()

# Muallif.objects.all().order_by("tugulgan_kun").first()

# Kitob.objects.filter(janr = "Badiiy").order_by("sahifa").first()

# Muallif.objects.filter(tirik="True").first()

# Talaba.objects.filter(kurs = 4).order_by("-kitob_soni").first()

# import datetime
#
# h_sana = str(datetime.date.today())
# yil = h_sana[:4]
# kerakli_sana = h_sana.replace(yil, str(int(yil)-45))
# print(h_sana, kerakli_sana)


# talaba = Talaba(ism = "Aziz", kurs = 2, kitob_soni = 3).save()
# Muallif.objects.create(ism = "A.Qodiriy", jins = "Erkak", kitoblar_soni = 13, tirik = False )


