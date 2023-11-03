from django import forms
from . models import *

class ToDoForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['name', 'priority', 'date']