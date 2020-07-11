from django import forms
from .models import URLs

class URLForm(forms.ModelForm):
    target_url = forms.URLField(required=True, max_length=100000, label='Your URL')
    utm_campaign = forms.CharField(required=False, label='Your UTM campaign')
    source = forms.CharField(
        required=False, max_length=100, label='Your UTM source')
    utm_medium = forms.CharField(
        required=False, max_length=100, label='Your UTM medium')

    class Meta:
        # Provide the association between a model form and a model
        model = URLs
        fields = ("target_url", "utm_campaign", "source", "utm_medium")

