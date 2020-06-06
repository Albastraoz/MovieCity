from django import forms
from .models import AddMovie

# This is the form used on the html page to show the form.
class AddMovieForm(forms.ModelForm):
    class Meta:
        model = AddMovie
        fields = ('search_field',)