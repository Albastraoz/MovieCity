from django import forms

# This is the form used on the html page to show the form.
class SearchForm(forms.Form):
    search_field = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Search by movie title...'}))