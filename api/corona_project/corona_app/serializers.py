from rest_framework import serializers
from corona_app.models import CoronaApp, MedicalMap, LANGUAGE_CHOICES, STYLE_CHOICES


class CoronaAppSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100, default='a')
    status = serializers.IntegerField(default=0)
    
    latitude= serializers.FloatField(default=0)
    longitude= serializers.FloatField(default=0)
    diabetes = serializers.BooleanField(default=False)

    #required=True, 

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CoronaApp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.diabetes = validated_data.get('diabetes', instance.diabetes)
        
        instance.save()
        return instance


# class MedicalMapSerializer(serializers.Serializer):

#     age = serializers.IntegerField(default=0, style={'placeholder': 'Age'})

#     # GENDER, AGE, HEIGHT, WEIGHT
#     # self_else = np.random.randint(0,2)
#     # gender = np.random.randint(0,2)
#     #gender = np.where(gender==0, -1, gender)
#     height = serializers.IntegerField(default=0, style={'placeholder': 'Height'})
#     weight = serializers.IntegerField(default=0, style={'placeholder': 'Weight'})


#     #Prev Conditions
#     #Diabetes
#     diabetes = serializers.BooleanField(default=False, style={'placeholder': 'Diabetes'})

#     #Kidney
#     kidney = serializers.BooleanField(default=False, style={'placeholder': 'Kidney'})
#     #Heart
#     heart = serializers.BooleanField(default=False, style={'placeholder': 'Heart'})
#     #Lungs
#     lungs = serializers.BooleanField(default=False, style={'placeholder': 'Lungs'})
#     #Stroke
#     stroke = serializers.BooleanField(default=False, style={'placeholder': 'Stroke'})
#     #Hypertension
#     hypertension =  serializers.BooleanField(default=False, style={'placeholder': 'Hypertension'})

#     #Immunocompromised
#     #HIV
#     hiv = serializers.BooleanField(default=False, style={'placeholder': 'HIV'})
#     #Transplant
#     transplant = serializers.BooleanField(default=False, style={'placeholder': 'Transplant'})

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return MedicalMap.objects.create(**validated_data)


