# Generated by Django 4.1.7 on 2023-03-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]