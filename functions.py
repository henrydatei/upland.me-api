import requests

def login(email, password):
    jsondata = {"email": email, "password": password, "strategy": "local"}
    req = requests.post('https://api.upland.me/authentication', json=jsondata)
    req.raise_for_status()
    return req.text

def getDashboard(token):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/dashboard', headers=headers)
    req.raise_for_status()
    return req.text

def renewVisa(token):
    headers={"authorization": "Bearer "+token}
    req = requests.post('https://api.upland.me/users/visa', headers=headers)
    req.raise_for_status()
    return req.text
