# Generated by Django 4.2.3 on 2023-07-06 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patientId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('scan', models.ImageField(blank=True, null=True, upload_to='scan_images')),
                ('phone', models.CharField(max_length=200)),
                ('dateOfBirth', models.DateField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
    ]