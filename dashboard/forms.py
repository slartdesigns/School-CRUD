from django import forms

class registerForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput,label='Nombre/s')
    last_name=forms.CharField(widget=forms.TextInput,label='Apellidos/s')
    password=forms.CharField(widget=forms.PasswordInput,label='Contraseña')

