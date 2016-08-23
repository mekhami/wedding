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
