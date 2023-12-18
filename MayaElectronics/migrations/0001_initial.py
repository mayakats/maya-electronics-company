# Generated by Django 3.2.21 on 2023-11-14 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('salutation', models.CharField(max_length=255)),
                ('fullname', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('username', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=255)),
                ('marital_status', models.CharField(max_length=255)),
                ('job_role', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MayaElectronics.department')),
            ],
        ),
    ]