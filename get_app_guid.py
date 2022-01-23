import json
from cf_oauth_token import cf_oauth_token
import requests


def get_app_guid(token, app):
    url = f"https://api.cf.sap.hana.ondemand.com/v3/apps?page=1&per_page=1000&space_guids=2c92d3e7-a833-4fbf-89e2-917c07cea220&names={app}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    guid = json.loads(response.text)["resources"][0]["guid"]

    return guid


def main():
    oauth_token = cf_oauth_token()
    app_name = input("app_name- ")
    print(get_app_guid(oauth_token, app=app_name))


if __name__ == "__main__":
    main()
