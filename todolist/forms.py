from django import forms

class CreateTask(forms.Form):
    title = forms.CharField(label='Title')
    description = forms.CharField(label='Description')