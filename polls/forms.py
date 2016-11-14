from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.Textarea)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True,widget=forms.Textarea)
    mensaje = forms.CharField(required=True,widget=forms.Textarea)