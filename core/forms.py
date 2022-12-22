from django import forms

class Login(forms.Form):
    usuario = forms.CharField(label='usuario', max_length=100)
    senha = forms.CharField(label='senha', max_length=20)