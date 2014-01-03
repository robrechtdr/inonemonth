# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Form
from userena.forms import SignupFormOnlyEmail
from apps.core import send_mail


class SignupForm(SignupFormOnlyEmail):
    first_name = forms.CharField(label='',
                                 max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'First name'}))

    last_name = forms.CharField(label='',
                                max_length=30,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Last name'}))

    email = forms.EmailField(label='',
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder':'Email'}))

    password1 = forms.CharField(label='',
                                max_length=30,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    password2 = forms.CharField(label='',
                                max_length=30,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))

    # instance argument causes error in wizardview
    def __init__(self, instance, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        #del self.fields['password2']
        # Put the first and last name at the top
        new_order = self.fields.keyOrder[:-2]
        new_order.insert(0, 'first_name')
        new_order.insert(1, 'last_name')
        self.fields.keyOrder = new_order

    def save(self):
        user = super(SignupForm, self).save()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        send_mail.send_signup_email(user)

    class Meta:
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


