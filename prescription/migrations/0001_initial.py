# Generated by Django 4.2.3 on 2023-07-07 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('physicians', '0002_physician_createdat_physician_created_by_and_more'),
        ('pharmacies', '0001_initial'),
        ('checkup', '0001_initial'),
        ('patients', '0002_patients_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescriptionID', models.AutoField(primary_key=True, serialize=False)),
                ('drugName', models.CharField(max_length=200)),
                ('prescription', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('diagnosesID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkup_id', to='checkup.checkupdetail')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='physicians.physician')),
                ('patientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patients')),
                ('pharmacyID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacies.pharmacy')),
            ],
            options={
                'verbose_name_plural': 'prescriptions',
            },
        ),
    ]
