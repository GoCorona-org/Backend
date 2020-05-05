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


def home(request):
    status = True

    if not request.user.is_authenticated:
        return HttpResponseRedirect('admin')

    storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    try:
        access_token = credential.access_token
        resp, cont = Http().request("https://www.googleapis.com/auth/gmail.readonly",
                                    headers={'Host': 'www.googleapis.com',
                                            'Authorization': access_token})
    except:
        status = False
        print('Not Found')

    return Response(status)
    # return render(request, 'index.html', {'status': status})


################################
#   GMAIL API IMPLEMENTATION   #
################################

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>


FLOW = flow_from_clientsecrets(
    settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
    scope='https://www.googleapis.com/auth/gmail.readonly',
    redirect_uri='http://127.0.0.1:8000/oauth2callback',
    prompt='consent')


def gmail_authenticate(request):
    storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                       request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        service = build('gmail', 'v1', http=http)
        print('access_token = ', credential.access_token)
        status = True

        return render(request, 'index.html', {'status': status})


def auth_return(request):
    get_state = bytes(request.GET.get('state'), 'utf8')
    if not xsrfutil.validate_token(settings.SECRET_KEY, get_state,
                                   request.user):
        return HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.GET.get('code'))
    storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
    storage.put(credential)
    print("access_token: %s" % credential.access_token)
    return HttpResponseRedirect("/")