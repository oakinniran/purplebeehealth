# Generated by Django 4.2.3 on 2023-07-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
    ]