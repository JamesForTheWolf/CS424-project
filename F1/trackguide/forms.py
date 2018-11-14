from django import forms
from trackguide.models import Track

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude=['name', 'length']
