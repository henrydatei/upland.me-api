from functions import *
from itertools import chain
import json

accounts = ["email1:pass1", "email2:pass2"]

# downloasd all treasures
email = accounts[0].split(":")[0]
password = accounts[0].split(":")[1]
token = json.loads(login(email, password))['accessToken']
treasures = json.loads(getNearbySends(token, 37.80857842412992, 37.70490690979908, -122.38437277555661, -122.50744106601444)) # complete SF

for account in accounts:
    props = []
    email = account.split(":")[0]
    password = account.split(":")[1]

    token = json.loads(login(email, password))['accessToken']

    # get a list of all properties in range
    properties = json.loads(getPropertiesInRange(token))
    props = properties['props'][0]

    # search in treasure-list for properties in range
    print("Treasures for " + email)
    for i in treasures:
        if i['prop_id'] in props:
            print(i['prop_id'])
            id = i['id']
            print(id)
            collectedSends = json.loads(collectSendTreasure(token, id))['collected_count']
            print(collectedSends)
    del props[:]
