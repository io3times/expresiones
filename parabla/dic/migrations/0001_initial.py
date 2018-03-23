# Generated by Django 2.0.3 on 2018-03-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slowo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slowo_slowo', models.CharField(max_length=50)),
                ('slowo_czesc', models.CharField(choices=[('Czas.', 'Czasownik'), ('Rzecz.', 'Rzeczownik'), ('Przym.', 'Przymiotnik'), ('Drob.', 'Drobnica')], default='Drob.', max_length=20)),
                ('slowo_zdanie', models.TextField()),
            ],
        ),
    ]