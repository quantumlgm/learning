from celery import Celery

from config import settings


celery_app = Celery("demo")
celery_app.config_from_object(settings.model_dump())
