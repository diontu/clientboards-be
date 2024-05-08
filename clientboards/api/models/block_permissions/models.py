from django.db import models

from clientboards.api.models.accounts.models import Accounts
from clientboards.api.models.blocks.models import Blocks


# Create your models here.
class BlockPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    block_id = models.ForeignKey(Blocks, on_delete=models.CASCADE)
    account_id = models.OneToOneField(
        Accounts, on_delete=models.CASCADE, null=True, blank=True)
    permission_type = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    additional_conditions = models.JSONField()
