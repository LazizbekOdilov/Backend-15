# 11 --> Kitob.objects.filter(janr = "Badiiy").update(sahifa = 350)

# 15 -->Talaba.objects.filter(id = random.randrange(1,5)).update(kurs = 4)

# 16 -->kitoblar = Kitob.objects.filter(sahifa__lt=300)
#         for kitob in kitoblar:
#             kitob.sahifa += 50
#             kitob.save()




