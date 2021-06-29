import json
from datetime import datetime, timedelta
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.runtime.http.request_options import RequestOptions


# https://pypi.org/project/Office365-REST-Python-Client/
class APIPoint:

    def login(self):
        site_url = ""
        ctx = ClientContext(site_url).with_credentials(UserCredential("", ""))
        request = RequestOptions("{0}/_api/files".format(site_url))
        response = ctx.execute_request_direct(request)
        js = json.loads(response.content)
        web_title = js['d']['results']
        for i in web_title:
            for attribute, value in i.items():
                if attribute == 'TimeLastModified':
                    timeStamp = value

                    print("Time Sharepoint:" + timeStamp)
                    print("Time Python:    " + str(datetime.now()))
                    if timeStamp < str(datetime.now() - timedelta(hours=10)):
                        print("Hi")
                if attribute == 'Url':
                    fileName = str(value).split('/')[-1]
                    print(fileName)


apiTest = APIPoint()
apiTest.login()
