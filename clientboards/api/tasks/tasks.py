from celery import shared_task


@shared_task
def log(message):
    print(message)


@shared_task
def add(one, two):
    return one + two


@shared_task
def saveBlock(id: int, properties: dict, content: str):
    # TODO: save the block using the id, properties, and content
    pass
