from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Message', widget=forms.Textarea())
