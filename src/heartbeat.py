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
    interval = 58

while True:
    r = requests.get(url)
    print(r.json())
    sleep(interval)