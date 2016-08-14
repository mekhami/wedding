from django import forms

from .models import RSVP


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'email', 'attending', 'guests', 'address1', 'address2', 'city', 'zip_code',
                  'state', 'song_request']
        widgets = {
            'attending': forms.RadioSelect(
                choices=[(True, 'Yes'), (False, 'No')],
                attrs={'class': 'form-check-input'},
            )
        }
