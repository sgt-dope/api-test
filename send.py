import os
import time
import requests
from requests.auth import HTTPBasicAuth

comnd = os.popen('gp url')
curr_url = comnd.read().strip()

data = {"url":curr_url}
'''
For some reason, when deploying the REST API to heroku, it requires multiple POST requests for the url to be save
otherwise, it reverts to old links, or even empty list.
'''
for i in range(3):
    url_send = requests.post(
        url="https://fetch-url-ff.herokuapp.com/add",
        params=data,
        auth = HTTPBasicAuth(os.environ.get("AUTH_USERNAME"), os.environ.get("AUTH_PASSWORD"))
    )
    time.sleep(1)