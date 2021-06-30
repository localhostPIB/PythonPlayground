import json
import sched, time
import schedule
from itertools import islice
from datetime import datetime
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.runtime.http.request_options import RequestOptions


# https://pypi.org/project/Office365-REST-Python-Client/
class APIPoint:
    __timeStamp = None
    __ctx = None
    __site_url = None
    s = sched.scheduler(time.time, time.sleep)
    delay_seconds = 5

    def login(self):
        self.__site_url = "https"
        self.__ctx = ClientContext(self.__site_url).with_credentials(
            UserCredential("", "))

    def getWebTitle(self):
        request = RequestOptions("{0}/_api/files".format(self.__site_url))
        response = self.__ctx.execute_request_direct(request)
        js = json.loads(response.content)
        web_title = js['d']['results']

        return web_title

    def iterateJSON(self):
        web_title = self.getWebTitle()

        for i in web_title:
            for attribute, value in i.items():
                if attribute == 'TimeLastModified':
                    if self.__timeStamp < value:
                        self.__timeStamp = value

                        for k, v in islice(i.items(), 1, None):
                            if k == 'Name':
                                fileName = str(v)
                                print("Datei: " + fileName + " wurde geändert !")

    def init(self):
        web_title = self.getWebTitle()

        for i in web_title:
            for attribute, value in i.items():
                if attribute == 'TimeLastModified':
                    self.__timeStamp = value

                    print("Time Sharepoint:" + self.__timeStamp)
                    print("Time Python:    " + str(datetime.now()))


apiTest = APIPoint()
apiTest.login()
apiTest.init()
schedule.every(3).seconds.do(apiTest.iterateJSON)

while True:
    schedule.run_pending()
    time.sleep(1)
