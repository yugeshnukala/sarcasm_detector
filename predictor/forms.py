from django import forms

class Headline(forms.Form):
    headline = forms.CharField(widget=forms.TextInput(attrs={'id':'id-for-headline','placeholder':'Your headline'}))
