# Generated by Django 4.2.9 on 2024-03-01 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0048_deposit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit',
            old_name='user',
            new_name='username',
        ),
    ]