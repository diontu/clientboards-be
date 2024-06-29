from django.db import models

from clientboards.api.models.users.models import Users


class BlockType(models.TextChoices):
    PAGE = 'page'
    NOTIONDB = 'notiondb'
    DIVIDER = 'divider'
    TODO = 'todo'
    OLIST = 'olist'
    ULIST = 'ulist'
    BUTTON = 'button'
    HEADER = 'header'
    PARAGRAPH = 'paragraph'
    CALLOUT = 'callout'


# Create your models here.
class Blocks(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30, choices=[(
        choice.value, choice.name) for choice in BlockType])
    properties = models.JSONField()
    content = models.TextField()
    parent_id = models.OneToOneField(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    account_id = models.ForeignKey(Users, on_delete=models.CASCADE)
