# Generated by Django 3.0.5 on 2020-04-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoronaApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]