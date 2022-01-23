import json
import os
import time
import requests
from cf_oauth_token import cf_oauth_token
from get_app_guid import get_app_guid
from instancecount import instancecount

def scale_down_mtms(guid, token, instance_count):
    url = f"https://api.cf.sap.hana.ondemand.com/v3/processes/{guid}/actions/scale"

    payload = json.dumps({
        "instances": instance_count - 1
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    no_of_instances = (json.loads(response.text))["instances"]
    print(f"scaled down to {no_of_instances} instances")

def scale_up_mtms(guid, token, instance_count):
    url = f"https://api.cf.sap.hana.ondemand.com/v3/processes/{guid}/actions/scale"

    payload = json.dumps({
        "instances": instance_count + 1
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    no_of_instances = (json.loads(response.text))["instances"]
    print(f"scaled up to {no_of_instances} instances")


app_string = os.getenv("MTMS")
app_list = app_string.split(',')
# app_list = ["it-app-prov", "it-op-rest"]
no_of_apps = len(app_list)
print(f"you have selected {no_of_apps} apps to scale down.They are - {app_list}")
oauth = cf_oauth_token()

for app in app_list:
    guid = get_app_guid(oauth, app)
    instance_count = int(instancecount(guid,oauth))
    print(app)
    scale_down_mtms(guid, oauth, instance_count)

time.sleep(int(os.getenv("DOWNTIME")))

# time.sleep(60)

for app in app_list:
    guid = get_app_guid(oauth, app)
    instance_count = int(instancecount(guid, oauth))
    print(app)
    scale_up_mtms(guid, oauth,instance_count)