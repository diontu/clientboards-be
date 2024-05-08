from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    last_login = models.DateTimeField()
    date_created = models.DateTimeField()

    class Meta:
        db_table = 'users'
