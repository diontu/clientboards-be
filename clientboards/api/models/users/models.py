from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, unique=True)
    # bcrypt max length for hashed passwords
    password = models.CharField(max_length=72)
    country = models.CharField(max_length=50)
    last_login = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'users'
