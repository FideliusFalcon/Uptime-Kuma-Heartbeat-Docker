import requests
import os
from time import sleep
from sys import exit

try:
    url = os.getenv("push_url")
except:
    raise Exception("Push url is not given")
try:
    interval = os.getenv("push_interval")
    try:
        interval = int(interval)
    except:
        raise Exception("Interval is not a integer")
        exit
except:
    interval = 55

headers = {}
try:
    headers["CF-Access-Client-Id"] = os.getenv("cf_access_client_id")
    headers["CF-Access-Client-Secret"] = os.getenv("cf_access_client_secret")
except:
    pass

while True:
    r = requests.get(url, headers = headers)
    print(r.status_code)
    sleep(interval)