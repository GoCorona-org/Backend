#!/bin/bash
# Command should be run from this folder else error out
# TODO : Dockerize the file

cd ../../api
pip3 install --no-cache-dir -r requirements.txt
python3 manage.py makemigrations medicalmap
python3 manage.py sqlmigrate medicalmap 0001_initial
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
