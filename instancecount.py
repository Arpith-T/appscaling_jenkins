import json

import requests


def instancecount(guid, token):
    url = f"https://api.cf.sap.hana.ondemand.com/v3/apps/{guid}/processes"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)["resources"][0]["instances"]
