# Generated by Django 4.1.3 on 2023-02-26 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicalmain', '0004_alter_doctor_specialitie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(default='', max_length=100)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('doctName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalmain.doctor')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalmain.specialities')),
            ],
        ),
    ]
