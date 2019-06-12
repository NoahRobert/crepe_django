from django import forms

class ContactForm(forms.Form):
    url = forms.URLField()
    pseudo = forms.CharField(max_length=100)

