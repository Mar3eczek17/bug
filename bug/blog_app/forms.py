from django.forms import ModelForm, TextInput

from .models import Wiadomosc


class EdytujWiadomoscForm(ModelForm):
    class Meta:
        model = Wiadomosc
        fields = ['tekst', 'created_date']
        exclude = ['author']
        widgets = {'tekst': TextInput(attrs={'size': 60})}
