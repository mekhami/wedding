import celery
import os

from django.conf import settings
from django.core.mail import EmailMessage

FROM_EMAIL = settings.EMAIL_HOST_USER

app = celery.Celery('tasks', broker=os.environ.get('REDIS_URL'), backend=os.environ.get('REDIS_URL'))


@app.task
def send_not_attending_notification(name):
    subject = '{} is not attending'.format(name)
    body = '{} has RSVPd and they will not be attending'.format(name)
    email = EmailMessage(subject, body, FROM_EMAIL, ('thevanderpod@gmail.com',))
    email.send()


def send_guest_email(email_address):
    subject = 'Thanks for RSVPing!'
    body = 'Thanks for RSVPing to our wedding! We\'ll send more information soon regarding \
            accomodations, locations, menu, and more. If you have any questions, feel free to send \
            us an email or give us a call!'
    email = EmailMessage(subject, body, FROM_EMAIL, (email_address,))
    email.send()


def send_notification(name, guests):
    subject = '{} has RSVP\'d!'.format(name)
    body = '{} has RSVP\'d with {} guest(s)'.format(name, guests)
    email = EmailMessage(subject, body, FROM_EMAIL, ('thevanderpod@gmail.com',))
    email.send()
