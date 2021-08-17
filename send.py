import os
import requests

comnd = os.popen('gp url')
curr_url = comnd.read().strip()

data = {"url":curr_url}

for i in range(2):
    url_send = requests.post(
        url="https://fetch-url-ff.herokuapp.com/add",
        params=data
    )