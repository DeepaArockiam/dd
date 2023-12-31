# forms.py
from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'grade', 'location']
