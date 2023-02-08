# Generated by Django 4.1.6 on 2023-02-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admirer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('location', models.TextField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='thirsty',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='plant',
            name='admirers',
            field=models.ManyToManyField(to='main_app.admirer'),
        ),
    ]
