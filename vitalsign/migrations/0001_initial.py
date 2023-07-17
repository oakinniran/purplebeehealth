# Generated by Django 4.2.3 on 2023-07-17 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('specialisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VITALSIGN',
            fields=[
                ('vitalSignId', models.AutoField(primary_key=True, serialize=False)),
                ('bloodPressure', models.IntegerField()),
                ('weight', models.CharField(max_length=200)),
                ('pulseRate', models.FloatField()),
                ('height', models.CharField(max_length=200)),
                ('temperature', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('bloodSugar', models.CharField(max_length=200)),
                ('updatedAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='patients.patients')),
                ('specialisatiion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialisations.specialisation')),
            ],
        ),
    ]
