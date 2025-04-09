from django import forms
from .models import OnayDefterKayitModel

class OnayDefterKayitForm(forms.ModelForm):
    class Meta:
        model = OnayDefterKayitModel
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }