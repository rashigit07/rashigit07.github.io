# Generated by Django 2.2.6 on 2019-10-07 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(max_length=50)),
                ('University', models.CharField(max_length=60)),
                ('Score', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Year_passing', models.IntegerField()),
            ],
        ),
    ]