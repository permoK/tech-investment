# Generated by Django 4.2.10 on 2024-03-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0057_withdrawalrequest_delete_amountwithdrawn'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawalrequest',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]