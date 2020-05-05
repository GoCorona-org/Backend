# Create your views here.
from medicalmap.models import MedicalMap
# , CredentialsModel
from medicalmap.serializers import MedicalMapSerializer
from medicalmap.calculations import MedicalScoreCalculator
from spotcorona import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django_pandas.io import read_frame
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage

import numpy as np
import pandas as pd
import glob, os
import csv, json
import httplib2



class MedicalList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        # snippets = MedicalMap.objects.all()
        # serializer = MedicalMapSerializer(snippets, many=True)
        # return Response(serializer.data)
        return Response("Post Medical Data here")

    def post(self, request, format=None):
        ### Removal of this line maybe necessary
        
        serializer = MedicalMapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, med_uuid, format=None):
        snippet = MedicalMap.objects.get(med_uuid = med_uuid)
        serializer = MedicalMapSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, med_uuid, format=None):
        snippet = MedicalMap.objects.get(med_uuid = med_uuid)
        serializer = MedicalMapSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            snippet.travel_filled = True
            snippet.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, med_uuid, format=None):
        snippet = MedicalMap.objects.get(med_uuid = med_uuid)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TravelList(APIView):
    def get(self, request, file, format=None):
        filename = file + '.csv'
        with open(filename, mode='r') as infile:
            reader = csv.reader(infile)
            file_list = [rows[0] for rows in reader]

        return Response(file_list)

class MedicalResult(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, med_uuid, format=None):
        snippet = MedicalMap.objects.get(med_uuid = med_uuid)
        # serializer = MedicalMapSerializer(snippet)
        F, Shades, prob = MedicalScoreCalculator(snippet)
        score_json = {"score": str(F), "score_color": Shades, "probability": str(prob)}
        return JsonResponse(score_json, safe=False)