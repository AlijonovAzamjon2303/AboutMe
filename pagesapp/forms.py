from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=300)
    last_name = forms.CharField(label='Last Name', max_length=300)