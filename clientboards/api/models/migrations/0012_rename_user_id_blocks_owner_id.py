# Generated by Django 5.0.4 on 2024-07-05 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_blocks_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blocks',
            old_name='user_id',
            new_name='owner_id',
        ),
    ]
