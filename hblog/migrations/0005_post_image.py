# Generated by Django 4.0.6 on 2024-05-14 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hblog', '0004_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
