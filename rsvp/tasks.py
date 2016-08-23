import celery
import os


app = celery.Celery('tasks', broker=os.environ.get('REDIS_URL'), backend=os.environ.get('REDIS_URL'))


@app.task
def add(x, y):
    return x + y
