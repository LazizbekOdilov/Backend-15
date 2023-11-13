from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def homepage(request):
    return render(request, "home.html")


def hamma_yonalishlar(request):
    if request.method == 'POST':
        forma = YonalishForm(request.POST)
        if forma.is_valid():
            data = forma.cleaned_data
            Yonalish.objects.create(
                nom=data.get("nom"),
                aktiv=data.get("aktiv"),
            )

    # if request.method == 'POST':
    #     Yonalish.objects.create(
    #         nom=request.POST.get("nom"),
    #         aktiv=request.POST.get("aktiv") == "on",
    #     )
    content = {
        "yonalishlar": Yonalish.objects.all(),
        "forma": YonalishForm()
    }
    return render(request, "hamma_yonalishlar.html", content)


def yonalish_ochir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect("/hamma_yonalishlar/")


def yonalish_update(request, son):
    if request.method == 'POST':
        Yonalish.objects.filter(id=son).update(
            nom=request.POST.get("nom"),
            aktiv=request.POST.get("aktiv") == "on",
        )
        return redirect('/hamma_yonalishlar/')

    content = {
        "yonalish": Yonalish.objects.get(id=son)
    }
    return render(request, 'yonalish_update.html', content)


def hamma_fanlar(request):
    if request.method == 'POST':
        forma = FanForm(request.POST)
        if forma.is_valid():
            forma.save()


    # if request.method == 'POST':
    #     Fan.objects.create(
    #         nom=request.POST.get("nom"),
    #         yonalish=Yonalish.objects.get(id=request.POST.get("yonalish")),
    #         asosiy=request.POST.get("asosiy") == "on",
    #     )
    soz = request.GET.get("qidirish_sozi")
    natija = Fan.objects.all()
    if soz:
        natija = natija.filter(nom__contains=soz)
    content = {
        "fanlar": natija,
        "yonalishlar": Yonalish.objects.all(),
        "forma":FanForm()
    }
    return render(request, "hamma_fanlar.html", content)


def fan_ochir(request, son):
    Fan.objects.get(id=son).delete()
    return redirect("/hamma_fanlar/")


def fan_update(request, son):
    if request.method == 'POST':
        Fan.objects.filter(id=son).update(
            nom=request.POST.get("nom"),
            yonalish=Yonalish.objects.get(id=request.POST.get("yonalish")),
            asosiy=request.POST.get("asosiy") == "on",
        )
        return redirect('/hamma_fanlar/')

    content = {
        "fan": Fan.objects.get(id=son),
        "yonalishlar": Yonalish.objects.all()

    }
    return render(request, 'fan_update.html', content)


def hamma_ustozlar(request):
    if request.method == 'POST':
        Ustoz.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            yosh=request.POST.get("yosh"),
            daraja=request.POST.get("daraja"),
            fan=Fan.objects.get(id=request.POST.get("fan")),
        )
    soz = request.GET.get("qidirish_sozi")
    natija = Ustoz.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)
    content = {
        "ustozlar": natija,
        "fanlar": Fan.objects.all()
    }
    return render(request, "hamma_ustozlar.html", content)


def ustoz_update(request, son):
    if request.method == 'POST':
        Ustoz.objects.filter(id=son).update(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            yosh=request.POST.get("yosh"),
            daraja=request.POST.get("daraja"),
            fan=Fan.objects.get(id=request.POST.get("fan")),
        )
        return redirect('/hamma_ustozlar/')

    content = {
        "ustoz": Ustoz.objects.get(id=son),
        "fanlar": Fan.objects.all(),
        "jins": ["Erkak", "Ayol"],
        "daraja": ["Bakalavr", "Magistr", "Professor"]
    }
    return render(request, 'ustoz_update.html', content)
