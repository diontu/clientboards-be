# makes sure that celery is imported
from .celery import app as celery_app

__all__ = ['celery_app']