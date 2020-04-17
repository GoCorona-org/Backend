from django.shortcuts import render

# Create your views here.
from corona_app.models import CoronaApp, MedicalMap
from corona_app.serializers import CoronaAppSerializer
from corona_app.forms import MedicalMapForm
from corona_app.calculations import intersection_calculator, MedicalScoreCalculator
from rest_framework import mixins
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_pandas.io import read_frame

import geopandas as gpd
from geopandas import GeoDataFrame, GeoSeries, overlay
from shapely.geometry import Point, Polygon
import numpy as np
import pandas as pd
import glob, os
import csv


class CoronaAppList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    
    queryset = CoronaApp.objects.all()
    serializer_class = CoronaAppSerializer

    def get(self, request, *args, **kwargs):
    	CoronaApp.objects.all().delete()

    	for subdir, dirs, files in os.walk("user_location_data"):
    		for file in files:
    			file_path = "user_location_data" + os.sep + file
    			data_file = open(file_path , 'r')       
    			data = data_file.read()
    			data = eval(data)
    			for times in data["location_history"]:
    				app_data = {'uuid': data['id'], 'timeslot': times['timeslot'], 'status': times['status'], 'latitude': times['lat'], 'longitude': times['long']}
    				print(app_data)
    				serializer = CoronaAppSerializer(data = app_data)
    				if serializer.is_valid():
    					serializer.save()
    					print("saved")

    	return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CoronaAppDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = CoronaApp.objects.all()
    serializer_class = CoronaAppSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CoronaAppTimeslots(APIView):
	
	def get(self, request, format=None):
		value_list = CoronaApp.objects.values_list('timeslot', flat=True).distinct()
		print(value_list)
		return Response(value_list)


	

class CoronaAppResult(APIView):
	
	def get(self, request, timeno, format=None):
		value_list = CoronaApp.objects.values_list('timeslot', flat=True).distinct()
		# data = CoronaApp.objects.get(timeslot = value_list[int(timeno)])
		data = CoronaApp.objects.filter(timeslot__startswith = value_list[int(timeno)])
		data_frame = read_frame(data)            # Transform queryset into pandas dataframe 
		data_frame.rename(columns={'uuid': 'UUID', 'status': 'Status', 'latitude': 'Lat', 'longitude': 'Lng'}, inplace=True)
		# data_frame.drop(['id'], axis=1)

		# ISSUE DETECTED IN 89: drop.['Status_1','UUID_1','Lat_1','Lng_1'] NOT FOUND IN AXIS. UNCOMMENT FOLLOWING LINES ONCE ERROR RESOLVED
		infected = intersection_calculator(data_frame)
		return Response(infected)

		# return Response(data_frame)              # Return the result in JSON via Django REST Framework




def MedicalMapFormView(request):
	form = MedicalMapForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {'form' : form}
	return render(request, 'corona_app/medical_data.html', context)


def MedicalMapFormDetail(request, id):
	map = MedicalMap.objects.get(id = id)

	F, Shades = MedicalScoreCalculator(map)
	
	context = {'medmap': map, 'score': F, 'score_color': Shades}

	return render(request, 'corona_app/medical_result.html', context)



