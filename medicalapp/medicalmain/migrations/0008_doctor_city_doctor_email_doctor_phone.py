# Generated by Django 4.1.3 on 2023-03-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalmain', '0007_appointment_email_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
    ]