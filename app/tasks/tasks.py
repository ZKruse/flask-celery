from celery import Celery
from app.tasks import celeryconfig
from app.tokencontext import tokencontext
app = Celery('tasks')# , config_source=celeryconfig)

app.config_from_object(celeryconfig.__name__)

@app.task
def add(x, y):
    return x + y

@app.task
def hello(x, y, z):
  token = tokencontext.get()
  return token
    # return x + y + z