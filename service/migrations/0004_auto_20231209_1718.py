# Generated by Django 3.1.4 on 2023-12-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20231209_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='fname',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastname',
            field=models.CharField(max_length=10),
        ),
    ]
