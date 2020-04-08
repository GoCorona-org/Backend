import requests, json
import pandas as pd
import numpy as np


# Make sure this does *NOT* end in /
server = "http://ec2-13-233-44-13.ap-south-1.compute.amazonaws.com:8000"

user = "admin"
data = {"username": user, "password":"admin123!@#"}
#url should *always* end in /
response = requests.post(url=f"{server}/auth-token/", data=data)
token = json.loads(response.text)["token"]
headers = {"Authorization":f"Token {token}"}

geo = requests.get(url=f"{server}/users/{user}", headers=headers)
# print(geo.text)


post_url = server + '/users/' + user  + '/geo/' 


df = pd.read_csv('bengaluru_latlng_test.csv')
data_len = df.shape[0]
print(data_len)
#d = df.values

for i in range(0, data_len):
	name_bar = df['name'][i]
	status_bar = df['status'][i]
	latitude_bar = df['latitude'][i]
	longitude_bar = df['longitude'][i]

	post_data = {'name': name_bar, 'status': status_bar, 'latitude': latitude_bar, 'longitude': longitude_bar}
	print(post_data)

	posted = requests.post(url=f"{server}/users/{user}/geo/", data= post_data, headers=headers)
