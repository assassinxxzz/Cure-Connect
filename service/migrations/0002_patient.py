# Generated by Django 3.1.4 on 2023-12-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(max_length=10)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('aadharnumber', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('add', models.TextField()),
                ('symptoms', models.TextField()),
                ('ename', models.CharField(max_length=30)),
                ('relation', models.CharField(max_length=30)),
                ('emergencynumber', models.CharField(max_length=10)),
            ],
        ),
    ]
