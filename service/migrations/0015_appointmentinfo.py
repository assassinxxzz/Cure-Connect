# Generated by Django 3.2.23 on 2024-01-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_delete_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointmentinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(max_length=50)),
                ('location', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]
