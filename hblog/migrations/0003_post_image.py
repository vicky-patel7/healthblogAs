# Generated by Django 4.0.6 on 2024-05-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hblog', '0002_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]