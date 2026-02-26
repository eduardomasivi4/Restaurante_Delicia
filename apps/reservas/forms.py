from django import forms
from phonenumber_field.formfields import PhoneNumberField

class Reserva(forms.Form):
    nome= forms.CharField(max_length=150)
    telefone= PhoneNumberField(region='AO')
    email= forms.EmailField()
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    pessoas= forms.IntegerField(min_value=1)
    observacoes= forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Alergias, Limitações...'}), required=False)
    