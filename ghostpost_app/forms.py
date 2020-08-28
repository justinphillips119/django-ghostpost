from django import forms
from ghostpost_app.models import GhostpostModel


class GhostpostForm(forms.ModelForm):
    class Meta:
        model = GhostpostModel
        fields = ["post_type", "content"]