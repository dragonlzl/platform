# Generated by Django 2.0.5 on 2018-05-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_phoneinfo_os'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneinfo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
