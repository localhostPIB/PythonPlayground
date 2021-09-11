import requests

request = '{ "driveId": "b!aNmA3PaUsUKiKLnhAL7aoBbj_q0BDm9PtWdRZ5h0bAn9bvU1K97UQoVLwBI7ilzQ","itemId": "0146M3IIZWKESJSXI3MBCILULWQ5Q2PXJ6","searchName": "doc",}'
header = {'Content-type': 'application/json', 'Accept': 'application/json'}
url = "http://c494-2001-16b8-20e2-7800-2dba-1199-59df-5ccb.ngrok.io/api/Search"
response = requests.post(url, data=request, headers=header)

print(response.json())
