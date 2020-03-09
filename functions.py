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

def myProperties(token):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/yield/mine', headers=headers)
    req.raise_for_status()
    return req.text

def myPropertiesDetailed(token):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/properties/mine/detailed', headers=headers)
    req.raise_for_status()
    return req.text

def getNearbyProperties(token,north,south,east,west):
    headers={"authorization": "Bearer "+token}
    parameters = {"north": north, "south": south, "east": east, "west": west}
    req = requests.get('https://api.upland.me/map', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text

def getNearbyPropertiesOnSale(token,north,south,east,west,sort_direction):
    headers={"authorization": "Bearer "+token}
    parameters = {"north": north, "south": south, "east": east, "west": west, "offset": 0, "limit": 20, "sort": sort_direction}
    req = requests.get('https://api.upland.me/properties/list-view', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text

def getPropertyInformation(token, prop_id):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/properties/{}'.format(prop_id), headers=headers)
    req.raise_for_status()
    return req.text

def findSuitableCollectionForProperty(token, prop_id):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/properties/match/{}'.format(prop_id), headers=headers)
    req.raise_for_status()
    return req.text

def getPriceForTeleportToProperty(token, prop_id):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/teleports/price/{}'.format(prop_id), headers=headers)
    req.raise_for_status()
    return req.text

def getNumberOfMessages(token):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/messages/count', headers=headers)
    req.raise_for_status()
    return req.text

def getStorePrices(token):
    headers={"authorization": "Bearer "+token}
    parameters = {"type": "upex"}
    req = requests.get('https://api.upland.me/store', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text