from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label="Search",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Type here...",
            'style': 'height: 30px; font-size: 18px; padding: 10px;border-radius:10px;'
        })
    )