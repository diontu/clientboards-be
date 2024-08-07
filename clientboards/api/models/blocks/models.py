from django.db import models

from clientboards.api.models.users.models import Users


class BlockType(models.TextChoices):
    PAGE = 'page'
    DIVIDER = 'divider'
    TODO = 'todo'
    OLIST = 'olist'
    ULIST = 'ulist'
    BUTTON = 'button'
    HEADER = 'header'
    PARAGRAPH = 'paragraph'
    CALLOUT = 'callout'

    INTEGRATION_NOTIONDB = 'integration_notiondb'
    # for the integration notiondb, client needs to pass the api token and the page id.
    # we store these values either in a new table that holds credentials from other integrations or in the same table. --> new database


# Create your models here.
class Blocks(models.Model):
    id = models.CharField(max_length=75, primary_key=True)
    type = models.CharField(max_length=30, choices=[(
        choice.value, choice.name) for choice in BlockType])
    properties = models.JSONField(blank=True)
    content = models.TextField(blank=True)
    parent_block_id = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    owner_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blocks'
