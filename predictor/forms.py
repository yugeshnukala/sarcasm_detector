from django import forms

class Headline(forms.Form):
    headline = forms.CharField(widget=forms.TextInput(attrs={'id':'headline','placeholder':'Your headline...','autofocus':'True'}))