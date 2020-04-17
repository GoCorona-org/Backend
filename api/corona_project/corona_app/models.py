from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.
#"UUID","Status","Lat","Lng"

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class CoronaApp(models.Model):
	uuid = models.CharField(max_length=1000, default='a')
	timeslot = models.CharField(max_length=100, default='00.00.01.01.2020')
	
	status = models.IntegerField(default=0)
	
	latitude= models.FloatField(default=0)
	longitude= models.FloatField(default=0)



class MedicalMap(models.Model):
    #name = models.CharField(max_length=100, blank=True, default='a')
    age = models.IntegerField(default=0)

    # GENDER, AGE, HEIGHT, WEIGHT
    # self_else = np.random.randint(0,2)
    # gender = np.random.randint(0,2)
    #gender = np.where(gender==0, -1, gender)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)


    #Prev Conditions
    #Diabetes
    diabetes = models.BooleanField(default=False)

    #Kidney
    kidney = models.BooleanField(default=False)
    #Heart
    heart = models.BooleanField(default=False)
    #Lungs
    lungs = models.BooleanField(default=False)
    #Stroke
    stroke = models.BooleanField(default=False)
    #Hypertension
    hypertension =  models.BooleanField(default=False)

    #Immunocompromised
    #HIV
    hiv = models.BooleanField(default=False)
    #Transplant
    transplant = models.BooleanField(default=False)



    #Symptoms
    


    #Fever

    class Fever(models.IntegerChoices):
        NO = 0, 'No'
        YES_OPT1 = 1, 'If Yes, then Temperature between 98.6 to 100.4 ^C'
        YES_OPT2 = 2, 'If Yes, then Temperature between 100.4 to 104 ^C'
        YES_OPT3 = 3, 'If Yes, then fever that comes and goes'
        YES_OPT4 = 4, 'If Yes, then have not checked the Temperature'

    fever = models.IntegerField(choices=Fever.choices, default=Fever.NO)



    #Cough

    class Cough(models.IntegerChoices):
        NO = 0, 'No'
        YES_OPT1 = 1, 'If Yes, then Dry Cough'
        YES_OPT2 = 2, 'If Yes, then Cough with sputum'
        YES_OPT3 = 3, 'If Yes, then Cough with chest pain'
        YES_OPT4 = 4, 'If Yes, then Cough with abdominal pain'

    cough = models.IntegerField(choices=Cough.choices, default=Cough.NO)


    #Shortness of breadth
    breathlessness  = models.BooleanField(default=False)

    #Fatigue
    fatigue = models.BooleanField(default=False)

    #Joint/Muscle pain
    joint_pain = models.BooleanField(default=False)

    #Loss of taste/smell          #Rare Case
    loss_of_taste_and_smell = models.BooleanField(default=False)

    # #Other Symptoms
    sore_throat = models.BooleanField(default=False)
    nasal_congestion = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    chills = models.BooleanField(default=False)
    nausea_or_vomiting = models.BooleanField(default=False)
    diarrhea = models.BooleanField(default=False)
    conjunctival_congestion = models.BooleanField(default=False)

    # #Improvement
    class Improvement(models.IntegerChoices):
        YES = 0, 'Improved'
        NO_OPT1 = 1, 'No change'
        NO_OPT2 = 2, 'Worsened'
        NO_OPT3 = 3, 'Worsened considerably'

    symptoms_improvement = models.IntegerField(choices=Improvement.choices, default=Improvement.YES)

    #Domestic Travel info
    #flight, train, auto, cab

    domestic_flight = models.BooleanField(default=False)
    domestic_train = models.BooleanField(default=False)
    domestic_auto = models.BooleanField(default=False)
    domestic_cab = models.BooleanField(default=False)

    domestic_airport_from = models.CharField(max_length=1000, blank=True, default=' ')
    domestic_airport_to = models.CharField(max_length=1000, blank=True, default=' ')
    current_state = models.CharField(max_length=1000, blank=True, default=' ')



    international_mode = models.BooleanField(default=False)
    country_travelled = models.CharField(max_length=1000, blank=True, default=' ')
    # gamma_inter = np.random.randint(1,100)



