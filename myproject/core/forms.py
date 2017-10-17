# -*- coding: utf-8 -*-
from django import forms
from django.forms import CharField, Form, PasswordInput
from .models import  Candidate

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'phone']