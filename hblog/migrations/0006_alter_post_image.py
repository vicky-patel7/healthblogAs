# Generated by Django 4.0.6 on 2024-05-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hblog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
