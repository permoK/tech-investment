# Generated by Django 4.2.10 on 2024-03-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0063_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='purchase',
            name='title',
            field=models.CharField(default=True, max_length=12),
        ),
    ]
