from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea)