
import uuid

from django.db import models

from clientboards.api.models.users.models import Users


# TODO: might not be the best way to create session ids
class Sessions(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4,
                                  editable=False, primary_key=True)
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='session')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        db_table = 'sessions'
