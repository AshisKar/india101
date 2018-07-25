from django import forms

from .models import Oppurtunities


class SearchForm(forms.ModelForm):
    caste = forms.CharField()
    annual_income = forms.CharField()

    class Meta:
        model = Oppurtunities
        fields = ['age_criteria', 'gender_criteria']