from django.db import models

from django import forms
class newtaskform(forms.Form):
    task = forms.CharField(max_length=200,label='Enter you new task')
    