import os
import time
import requests
from requests.auth import HTTPBasicAuth

comnd = os.popen('gp url 8080')
curr_url_kc = comnd.read().strip()

comnd2 = os.popen('gp url 5000')
curr_url_app = comnd2.read().strip()


payload = {"urls":{
    "keycloak_url":curr_url_kc,
    "app_url":curr_url_app
}}


'''
For some reason, when deploying the REST API to heroku, it requires multiple POST requests for the url to be save
otherwise, it reverts to old links, or even empty list.
'''

for i in range(10):
    url_send = requests.post(
        url="https://fetch-urls-ff.herokuapp.com/add",
        json=payload,
        auth = HTTPBasicAuth(os.environ.get("AUTH_USERNAME"), os.environ.get("AUTH_PASSWORD"))
    )
    time.sleep(0.2)