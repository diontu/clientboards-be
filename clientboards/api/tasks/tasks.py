from celery import shared_task


@shared_task
def log(message):
    print(message)

@shared_task
def add(one, two):
    return one + two