from django import forms

class CreateTask(forms.Form):
    title = forms.CharField(label='Title', widget=forms.Textarea(attrs={'placeholder' : "Task Title", 'rows':1, 'style':'resize:none'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder' : "Task Description", 'style':'resize:none'}))