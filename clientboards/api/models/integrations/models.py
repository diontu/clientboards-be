from django.db import models

from clientboards.api.models.blocks.models import BlockType
from clientboards.api.models.users.models import Users


class Integrations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, choices=[(
        choice.value, choice.name) for choice in BlockType])
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    attributes = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'integrations'
