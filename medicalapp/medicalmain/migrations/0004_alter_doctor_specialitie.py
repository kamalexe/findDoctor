# Generated by Django 4.1.3 on 2023-02-26 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicalmain', '0003_alter_doctor_specialitie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialitie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalmain.specialities'),
        ),
    ]