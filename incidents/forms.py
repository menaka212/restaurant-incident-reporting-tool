from django import forms
from .models import Incident


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }