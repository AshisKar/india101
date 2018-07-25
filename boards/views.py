from django.shortcuts import get_object_or_404, redirect, render

from .forms import  SearchForm
from .models import Oppurtunities


def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            gender_criteria = form.cleaned_data.get('gender_criteria')
            age_criteria = form.cleaned_data.get('age_criteria')
            oppurtunity = Oppurtunities.objects.filter(gender_criteria=gender_criteria, age_criteria=age_criteria )
            return render(request, 'results.html', {'oppurtunity': oppurtunity})
    else:
        form = SearchForm()

        return render(request, 'search_form.html', {'form': form})

