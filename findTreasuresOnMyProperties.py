from functions import *
import json

accounts = ["email1:pass1", "email2:pass2"]

# downloasd all treasures
email = accounts[0].split(":")[0]
password = accounts[0].split(":")[1]
token = json.loads(login(email, password))['accessToken']
treasures = json.loads(getNearbyTreasures(token, 37.80857842412992, 37.70490690979908, -122.38437277555661, -122.50744106601444)) # complete SF

for account in accounts:
    props = []
    email = account.split(":")[0]
    password = account.split(":")[1]

    token = json.loads(login(email, password))['accessToken']

    # get a list of all properties
    properties = json.loads(myProperties(token))
    for prop in properties:
        props.append(prop['prop_id'])

    # search in treasure-list for own properties
    print("Treasures for " + email)
    for i in treasures:
        if i['prop_id'] in props:
            print(i['prop_id'])
