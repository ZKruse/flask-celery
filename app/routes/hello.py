from flask import (Blueprint, request, session)
from app.tokencontext import tokencontext
from app.tasks.tasks import hello

bp = Blueprint('hello', __name__, url_prefix='/hello')

@bp.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
      token = request.args.get('token')
      print(token)
      tokencontext.set(token)
      task = hello.apply_async(args=['zac', 'was', 'here'])
      return {"Test": "zac was here", "TaskID": task.id}

