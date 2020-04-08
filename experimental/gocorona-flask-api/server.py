import requests
import json

from flask import Request, Response
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

server = "http://ec2-13-233-44-13.ap-south-1.compute.amazonaws.com:8000"
user = "admin"
data = {"username": user, "password":"admin123!@#"}
#url should *always* end in /

@app.route("/", methods=['GET', 'POST'])
def points_list():
    """
    List or create points.
    """
    if Request.method == 'POST':
        geo = requests.post(url=f"{server}/users/{user}", data=Request.data, headers=headers)
        return Response( geo.text , status=geo.status_code, mimetype='application/json')

    # request.method == 'GET'
    geo = requests.get(url=f"{server}/users/{user}", headers=headers)
    return Response( geo.text , status=geo.status_code, mimetype='application/json')

if __name__ == "__main__":
    response = requests.post(url=f"{server}/auth-token/", data=data)
    token = json.loads(response.text)["token"]
    headers = {"Authorization": f"Token {token}"}
    app.run(debug=True)