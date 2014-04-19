from django import forms

from .models import Campaign

class ListForm(forms.ModelForm):

    class Meta:
        model = Campaign
        include = ('name', 'slug', 'status', 'status_display', )
        #fields = ('name', 'desc', 'duration', )
