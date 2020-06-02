from django import forms
from django.forms import ModelForm

from .models import Book, Person
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()


class Enter(forms.Form):
    login = forms.CharField()


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)


"""class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'phone', 'city', 'mail', 'password']"""

