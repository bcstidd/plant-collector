# Generated by Django 4.1.6 on 2023-02-08 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('thrivesIn', models.CharField(max_length=250)),
                ('difficulty', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Thirsty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Watered')),
                ('water', models.CharField(choices=[('F', 'Fine'), ('W', 'Watered'), ('N', 'Not Watered')], default='F', max_length=1)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
        ),
    ]
