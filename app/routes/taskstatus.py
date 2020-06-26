from flask import (Blueprint, request, session)
from celery.result import AsyncResult

from app.tasks.tasks import app
from app.tokencontext import tokencontext

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/', methods=(['GET']))
def taskresult():
    if request.method == 'GET':
      task_id = request.args.get('id')
      print(task_id)
      result = AsyncResult(id=task_id, app=app)
      print(result)
      return {"result": result.get()}
