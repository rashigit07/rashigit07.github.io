# Generated by Django 2.2.6 on 2019-10-08 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0006_work_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_experience',
            name='Image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
    ]
