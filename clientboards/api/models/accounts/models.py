from django.db import models

# call the full path of the model to prevent circular import
from clientboards.api.models.users.models import Users


# Create your models here.
class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(
        Users, on_delete=models.CASCADE, related_name='account')
    attributes = models.TextField()  # JSON formatted string

    class Meta:
        db_table = 'accounts'
