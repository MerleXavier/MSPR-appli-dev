import requests
import os


# Retrieve public ip using the api ipify

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        print("Échec" + response.status_code)

# Print public ip

ip = get_public_ip()
print(ip)

# Set the DNS server to use

domain = ('cma4.box')

os.system(f"echo {domain} {ip} >> /etc/resolv.conf")
os.system('cat /etc/resolv.conf')
