from django.views.generic import CreateView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

from .models import RSVP
from .forms import RSVPForm


# Create your views here.
class RSVPCreateView(CreateView):
    template_name = 'rsvp/create.html'
    model = RSVP
    success_url = reverse_lazy('rsvp:thanks')
    form_class = RSVPForm

    def form_valid(self, form):
        attending = form.cleaned_data['attending']
        from_email = settings.EMAIL_HOST_USER
        to = (form.cleaned_data['email'],)
        if attending:
            subject = 'Thanks for RSVPing!'
            body = 'Thanks for RSVPing to our wedding! We\'ll send more information soon regarding \
                    accomodations, locations, menu, and more. If you have any questions, feel free to send \
                    us an email or give us a call!'
            email = EmailMessage(subject, body, from_email, to)
            email.send()

            subject = '{} has RSVP\'d!'.format(form.cleaned_data['name'])
            body = '{} has RSVP\'d with {} guest(s)'.format(form.cleaned_data['name'], form.cleaned_data['guests'])
            email = EmailMessage(subject, body, from_email, ('thevanderpod@gmail.com',))
            email.send()
        else:
            pass
        return HttpResponseRedirect(reverse_lazy('rsvp:thanks'))


def send_guest_email():
    pass


def send_notification():
    pass
