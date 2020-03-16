from django import forms
from .models import Coffee

class CreateCoffee(forms.ModelForm):
  class Meta:
    model = Coffee
    fields = '__all__'
