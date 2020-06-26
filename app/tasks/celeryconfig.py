
broker_url='amqp://user:bitnami@localhost:5672//'
result_backend='redis://localhost:6379/0'

task_routes = {
  'tasks.add': {},
  'app.routes.hello.hello': {},
}

worker_prefetch_multipler = 1
task_acks_late = True
task_create_missing_queues = True
broker_heartbeat = 0