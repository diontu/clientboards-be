from celery import shared_task


@shared_task
def log(message):
    print(message)