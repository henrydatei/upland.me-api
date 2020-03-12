import requests

userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"

def login(email, password):
    jsondata = {"email": email, "password": password, "strategy": "local"}
    headers = {'User-Agent': userAgent}
    req = requests.post('https://api.upland.me/authentication', json=jsondata, headers=headers)
    req.raise_for_status()
    return req.text

def register(email, password, username):
    # using the promo-code "cryptoticker" will give you 6000 UPX instead of 3000 UPX at the beginning
    jsondata = {"email": email, "password": password, "username": username, "ab_token": "cryptotickerpromo1", "promo_code": "cryptoticker"}
    headers = {'User-Agent': userAgent}
    req = requests.post('https://api.upland.me/users', json=jsondata, headers=headers)
    req.raise_for_status()
    return req.text

def getDashboard(token):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://api.upland.me/dashboard', headers=headers)
    req.raise_for_status()
    return req.text

def getMoney(token, account_id):
    headers={"authorization": "Bearer "+token}
    req = requests.get('https://multiindex-api.upland.me/accounts/{}'.format(account_id), headers=headers)
    req.raise_for_status()
    return req.text

def renewVisa(token):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.post('https://api.upland.me/users/visa', headers=headers)
    req.raise_for_status()
    return req.text

def myProperties(token):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://api.upland.me/yield/mine', headers=headers)
    req.raise_for_status()
    return req.text

def myPropertiesDetailed(token):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://api.upland.me/properties/mine/detailed', headers=headers)
    req.raise_for_status()
    return req.text

def getNearbyProperties(token,north,south,east,west):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    parameters = {"north": north, "south": south, "east": east, "west": west}
    req = requests.get('https://api.upland.me/map', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text

def getNearbyPropertiesClusters(token,north,south,east,west):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    parameters = {"north": north, "south": south, "east": east, "west": west, "clusters": "true"}
    req = requests.get('https://api.upland.me/map', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text

def getNearbyPropertiesOnSale(token,north,south,east,west,sort_direction):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    parameters = {"north": north, "south": south, "east": east, "west": west, "offset": 0, "limit": 20, "sort": sort_direction}
    req = requests.get('https://api.upland.me/properties/list-view', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text

def getNearbySends(token,north,south,east,west):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    parameters = {"north": north, "south": south, "east": east, "west": west}
    req = requests.get('https://treasures.upland.me/sends/discovery', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text

def getListOfTreasureStates(token):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://treasures.upland.me/treasures', headers=headers)
    req.raise_for_status()
    return req.text

def getTreasureHistory(token):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://treasures.upland.me/treasures/history', headers=headers)
    req.raise_for_status()
    return req.text

def getTreasureDirectionForProperty(token, prop_id):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://treasures.upland.me/treasures/direction/{}'.format(prop_id), headers=headers)
    req.raise_for_status()
    return req.text

def getPropertyInformation(token, prop_id):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://api.upland.me/properties/{}'.format(prop_id), headers=headers)
    req.raise_for_status()
    return req.text

def findSuitableCollectionForProperty(token, prop_id):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://api.upland.me/properties/match/{}'.format(prop_id), headers=headers)
    req.raise_for_status()
    return req.text

def getPriceForTeleportToProperty(token, prop_id):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://api.upland.me/teleports/price/{}'.format(prop_id), headers=headers)
    req.raise_for_status()
    return req.text

def getNumberOfMessages(token):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://api.upland.me/messages/count', headers=headers)
    req.raise_for_status()
    return req.text

def getStorePrices(token):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    parameters = {"type": "upex"}
    req = requests.get('https://api.upland.me/store', headers=headers, params=parameters)
    req.raise_for_status()
    return req.text

def isUnderMaintenance():
    req = requests.get('https://api.upland.me/settings/maintenance')
    req.raise_for_status()
    return req.text

def claimRewardForCompletedCollection(token, collection_id):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    jsondata = {"collection_id": collection_id}
    req = requests.post('https://api.upland.me/collections-completed/reward', json=jsondata, headers=headers)
    req.raise_for_status()
    return req.text

def getInformationAboutPlayer(token, username):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    req = requests.get('https://api.upland.me/profile/{}'.format(username), headers=headers)
    req.raise_for_status()
    return req.text

def putPropertyInCollection(token, collection_id, prop_id):
    headers={"authorization": "Bearer "+token, 'User-Agent': userAgent}
    jsondata = {"collection_id": collection_id, "prop_id": prop_id}
    req = requests.post('https://api.upland.me/coll-prop', json=jsondata, headers=headers)
    req.raise_for_status()
    return req.text
