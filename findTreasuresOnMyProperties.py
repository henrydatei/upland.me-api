from functions import *
import json

# I included Sendgrid to stay informed about new treasures on your property when using a cron job
# You need an Sendgrid API key, just follow the instructions on https://app.sendgrid.com/guide/integrate/langs/python
# Dont forget to enter your email in line 39 (to_emails='XXXXXX@XXXXXXX.XXXX')
# Remove the following 3 lines if you don't want to use Sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

            # Remove the following 9 lines of you don't want to use Sendgrid
            message = Mail(from_email='upland@upland.me', to_emails='XXXXXX@XXXXXXX.XXXX', subject='Found Treasure on Property', html_content="Username: " + email + ", prop_id: " + str(i['prop_id']))
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                #print(response.status_code)
                #print(response.body)
                #print(response.headers)
            except Exception as e:
                print(e.message)
