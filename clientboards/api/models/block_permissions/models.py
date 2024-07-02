from django.db import models

from clientboards.api.models.blocks.models import Blocks
from clientboards.api.models.users.models import Users


class BlockPermissionsType(models.TextChoices):
    READ = 'read'
    WRITE = 'write'


# Create your models here.
class BlockPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    block_id = models.ForeignKey(Blocks, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True, blank=True)
    permission_type = models.CharField(max_length=10, choices=[(
        choice.value, choice.name) for choice in BlockPermissionsType])
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    additional_conditions = models.JSONField()

    class Meta:
        db_table = 'block_permissions'
