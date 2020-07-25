from getpass import getpass
import requests




payload = {'name': 'n', 'password': '1234'}
r = requests.get('http://localhost:8080/user/check', params=payload)




print(r.text)