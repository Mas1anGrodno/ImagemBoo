from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class UserInspectForm(forms.ModelForm):
    email_confirm = forms.EmailField(label='Confirm Email', required=False)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='ReEnter Password', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email_confirm = cleaned_data.get('email_confirm')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if email and email_confirm and email != email_confirm:
            self.add_error('email_confirm', 'Email\'s does not match.')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Passwords\'s does not match.')
