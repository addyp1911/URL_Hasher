from django import forms
from .models import URLs
from .utils import url_validator

class URLForm(forms.ModelForm):
    target_url = forms.CharField(required=True, max_length=100000, label='Your URL', validators=[url_validator])
    utm_campaign = forms.CharField(required=False, label='Your UTM campaign')
    source = forms.CharField(
        required=False, max_length=100, label='Your UTM source')
    utm_medium = forms.CharField(
        required=False, max_length=100, label='Your UTM medium')

    class Meta:
        # Provide the association between a model form and a model
        model = URLs
        fields = ("target_url", "utm_campaign", "source", "utm_medium")


class SearchForm(forms.Form):
    search_url = forms.CharField(required=True, max_length=100000, label='Your URL', validators=[url_validator])
    search_keyword = forms.CharField(required=True, max_length=500, label='Your search keyword')

    class Meta:
        # Provide the association between a model form and a model
        fields = ("search_url", "search_keyword")