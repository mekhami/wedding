from django.views.generic import CreateView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

from .models import RSVP
from .forms import RSVPForm

FROM_EMAIL = settings.EMAIL_HOST_USER


# Create your views here.
class RSVPCreateView(CreateView):
    template_name = 'rsvp/create.html'
    model = RSVP
    success_url = reverse_lazy('rsvp:thanks')
    form_class = RSVPForm

    def form_valid(self, form):
        form.save()
        attending = form.cleaned_data['attending']
        if attending:
            send_guest_email(form.cleaned_data['email'])
            send_notification(
                form.cleaned_data['name'],
                form.cleaned_data['guests'],
                form.cleaned_data['attending']
            )
        else:
            send_not_attending_notification(form.cleaned_data['name'])
        return HttpResponseRedirect(reverse_lazy('rsvp:thanks'))


def send_guest_email(email):
    subject = 'Thanks for RSVPing!'
    body = 'Thanks for RSVPing to our wedding! We\'ll send more information soon regarding \
            accomodations, locations, menu, and more. If you have any questions, feel free to send \
            us an email or give us a call!'
    email = EmailMessage(subject, body, FROM_EMAIL, (email,))
    email.send()


def send_notification(name, guests):
    subject = '{} has RSVP\'d!'.format(name)
    body = '{} has RSVP\'d with {} guest(s)'.format(name, guests)
    email = EmailMessage(subject, body, FROM_EMAIL, ('thevanderpod@gmail.com',))
    email.send()


def send_not_attending_notification(name):
    subject = '{} is not attending'.format(name)
    body = '{} has RSVPd and they will not be attending'.format(name)
    email = EmailMessage(subject, body, FROM_EMAIL, ('thevanderpod@gmail.com',))
    email.send()
