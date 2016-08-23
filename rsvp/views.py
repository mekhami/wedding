from django.views.generic import CreateView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .models import RSVP
from .forms import RSVPForm
from . import tasks

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
            tasks.send_guest_email.delay(form.cleaned_data['email'])
            tasks.send_notification.delay(
                form.cleaned_data['name'],
                form.cleaned_data['guests'],
            )
        else:
            tasks.send_not_attending_notification.delay(form.cleaned_data['name'])
        return HttpResponseRedirect(reverse_lazy('rsvp:thanks'))
