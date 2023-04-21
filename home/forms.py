from django import forms
from .models import newsletter, contactus

class NewsletterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = newsletter
        fields = ['email']

class ContactusForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=120)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = contactus
        fields = ['name', 'email', 'subject','message']