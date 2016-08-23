import celery
import os


app = celery.Celery('tasks', broker=os.environ.get('REDIS_URL'), backend=os.environ.get('REDIS_URL'))


@app.task
def send_not_attending_notification(name):
    subject = '{} is not attending'.format(name)
    body = '{} has RSVPd and they will not be attending'.format(name)
    email = EmailMessage(subject, body, FROM_EMAIL, ('thevanderpod@gmail.com',))
    email.send()
