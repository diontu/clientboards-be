from celery import shared_task


@shared_task
def log(message):
    print(message)


@shared_task
def add(one, two):
    return one + two


@shared_task
def saveBlock(userId: int, type: str, properties: dict | None = None, content: str | None = None, parentId: int | None = None):
    # TODO: maybe could use **kwargs here
    # check if the block exists, if not create it
    print('hello from saveBlock')
    return 1
