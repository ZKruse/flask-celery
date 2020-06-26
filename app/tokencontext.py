import contextvars

tokencontext = contextvars.ContextVar('tokencontext', default='default')