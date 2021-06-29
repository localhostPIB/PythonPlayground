import requests
from requests.auth import HTTPBasicAuth


class APITest:

    def login(self):
        response = requests.get(
            url=r'',
            auth=HTTPBasicAuth("email", "PW " ),
            verify=cert)

        print(response.status_code)
