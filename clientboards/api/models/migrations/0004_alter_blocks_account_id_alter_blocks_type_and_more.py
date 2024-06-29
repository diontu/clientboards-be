# Generated by Django 5.0.4 on 2024-06-29 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_sessions_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocks',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
        migrations.AlterField(
            model_name='blocks',
            name='type',
            field=models.CharField(choices=[('page', 'PAGE'), ('notiondb', 'NOTIONDB'), ('divider', 'DIVIDER'), ('todo', 'TODO'), ('olist', 'OLIST'), ('ulist', 'ULIST'), ('button', 'BUTTON'), ('header', 'HEADER'), ('paragraph', 'PARAGRAPH'), ('callout', 'CALLOUT')], max_length=30),
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subscription_plan', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10)),
                ('billing_cycle', models.CharField(max_length=20)),
                ('billing_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=30)),
                ('trial_period', models.IntegerField(default=14)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='api.users')),
            ],
        ),
    ]
