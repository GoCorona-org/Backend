# Generated by Django 3.0.5 on 2020-04-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona_app', '0010_auto_20200416_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronaapp',
            name='timeslot',
            field=models.CharField(default='00.00.01.01.2020', max_length=100),
        ),
    ]
