# Generated by Django 4.1.3 on 2023-02-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalmain', '0005_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(default='', max_length=10),
        ),
    ]