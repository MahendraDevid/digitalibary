from django import forms
from .models import Ulasanbuku

class UlasanBukuForm(forms.ModelForm):
    class Meta:
        model = Ulasanbuku
        fields = ['ulasan', 'rating']
