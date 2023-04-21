from django import forms
from .models import RegisterUser


class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    family = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)
    code = forms.CharField(max_length=10)
    course_name = forms.CharField(max_length=10)

    class Meta:
        model = RegisterUser
        fields = ['name', 'family', 'phone','code', 'course_name']