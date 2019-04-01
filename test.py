# coding: utf-8
import requests
from datetime import datetime
import random
import time
time.sleep(1)
temp = 75
while True:
    temp = temp + random.randrange(5)
    requests.post("http://localhost:4000/", json={"temp": temp, "created_at": datetime.now().isoformat()})
    time.sleep(5)
