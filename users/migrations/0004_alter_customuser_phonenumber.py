# Generated by Django 4.2.3 on 2023-08-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
