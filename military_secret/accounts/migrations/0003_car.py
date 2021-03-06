# Generated by Django 3.1.7 on 2021-03-31 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210330_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
                ('wheel_type', models.CharField(choices=[('right', 'right'), ('left', 'left')], default='left', max_length=20)),
                ('car_type', models.CharField(choices=[('service', 'service'), ('daily', 'daily')], max_length=20)),
                ('car_number', models.CharField(max_length=25)),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dossier')),
            ],
        ),
    ]
