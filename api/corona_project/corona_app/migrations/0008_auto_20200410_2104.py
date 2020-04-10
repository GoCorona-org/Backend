# Generated by Django 3.0.5 on 2020-04-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona_app', '0007_auto_20200410_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalmap',
            name='airport_from',
        ),
        migrations.RemoveField(
            model_name='medicalmap',
            name='airport_to',
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='breathlessness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='chills',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='conjunctival_congestion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='cough',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'If Yes, then Dry Cough'), (2, 'If Yes, then Cough with sputum'), (3, 'If Yes, then Cough with chest pain'), (4, 'If Yes, then Cough with abdominal pain')], default=0),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='country_travelled',
            field=models.CharField(blank=True, default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='diarrhea',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='domestic_airport_from',
            field=models.CharField(blank=True, default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='domestic_airport_to',
            field=models.CharField(blank=True, default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='domestic_auto',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='domestic_cab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='domestic_flight',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='domestic_train',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='fatigue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='headache',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='international_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='joint_pain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='loss_of_taste_and_smell',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='nasal_congestion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='nausea_or_vomiting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='sore_throat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalmap',
            name='symptoms_improvement',
            field=models.IntegerField(choices=[(0, 'Improved'), (1, 'No change'), (2, 'Worsened'), (3, 'Worsened considerably')], default=0),
        ),
        migrations.AlterField(
            model_name='medicalmap',
            name='current_state',
            field=models.CharField(blank=True, default=' ', max_length=1000),
        ),
    ]