web: gunicorn payment_enabler.wsgi -b 0.0.0.0:$PORT
celeryd: python manage.py celeryd -E -B -l WARN
