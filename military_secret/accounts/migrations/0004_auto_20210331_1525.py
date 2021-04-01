# Generated by Django 3.1.7 on 2021-03-31 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='model',
            new_name='car_model',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('service', 'service'), ('private', 'private')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='country',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='dossier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.dossier'),
        ),
        migrations.AlterField(
            model_name='car',
            name='mark',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='wheel_type',
            field=models.CharField(choices=[('RH', 'right_hand'), ('LH', 'left_hand')], default='left', max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(default=2000),
        ),
    ]
