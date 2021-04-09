# Generated by Django 3.1.2 on 2021-04-09 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=255)),
                ('club_desc', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.club')),
            ],
        ),
    ]
