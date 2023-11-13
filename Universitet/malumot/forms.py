from django import forms

from .models import *


class YonalishForm(forms.Form):
    nom = forms.CharField(label="Nom")
    aktiv = forms.BooleanField(label="Aktiv")


class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = "__all__"
