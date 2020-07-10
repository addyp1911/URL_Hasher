from django import forms
from django.forms import Form


class URLForm(Form):
    url = forms.URLField(required=True, label='Your URL')
    utm_campaign = forms.CharField(required=False, label='Your UTM campaign')
    source = forms.CharField(
        required=False, max_length=100, label='Your UTM source')
    utm_medium = forms.CharField(
        required=False, max_length=100, label='Your UTM medium')

    def clean(self):
        cleaned_data = super(URLForm, self).clean()
        url = cleaned_data.get('url')
        utm_campaign = cleaned_data.get('utm_campaign')
        source = cleaned_data.get('source')
        utm_medium = cleaned_data.get('utm_medium')
        if not url:
            raise forms.ValidationError('You have to enter a valid URL!')
