from docker_pratica.celery_conf import app
from register.models import Register


@app.task(name='register', bind=True)
def register(self):
    try:
        Register.objects.create()
    except Exception as exc:
        raise self.retry(exc=exc, countdown=15)
