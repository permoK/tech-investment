# Generated by Django 3.2.21 on 2024-01-29 19:10

from django.db import migrations, models
import investor.utils


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0003_alter_userprofile_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='unique_code',
            field=models.CharField(default=investor.utils.generate_uuid, max_length=10, unique=True),
        ),
    ]