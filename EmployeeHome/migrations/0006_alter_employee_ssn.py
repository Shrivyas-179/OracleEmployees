# Generated by Django 3.2.7 on 2021-11-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeHome', '0005_auto_20211122_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ssn',
            field=models.IntegerField(max_length=100, null=True, unique=True),
        ),
    ]