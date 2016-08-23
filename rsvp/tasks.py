import celery
import os


app = celery.Celery('rsvp')
app.conf.update(BROKER_URL=os.environ['REDIS_URL'])


@app.task
def add(x, y):
    return x + y
