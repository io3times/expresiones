# Generated by Django 2.0.3 on 2018-03-19 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dic', '0002_auto_20180319_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zdanie',
            name='zdanie_slowo',
        ),
        migrations.AddField(
            model_name='slowo',
            name='slowo_zdanie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dic.Zdanie'),
        ),
        migrations.AlterField(
            model_name='zdanie',
            name='zdanie_zdanie',
            field=models.TextField(null=True),
        ),
    ]
