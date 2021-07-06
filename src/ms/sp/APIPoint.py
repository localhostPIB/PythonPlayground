import json
from itertools import islice

from src.ms.sp import StringUtils
from src.ms.sp.exceptions import LoginException
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.runtime.http.request_options import RequestOptions


# https://pypi.org/project/Office365-REST-Python-Client/
class APIPoint:
    __timeStamp = " "
    __ctx = None
    __site_url = None
    __count = 0

    def login(self):
        try:
            self.__site_url = StringUtils.StringUtils.websiteAPI
            self.__ctx = ClientContext(self.__site_url).with_credentials(
                UserCredential(StringUtils.StringUtils.email, StringUtils.StringUtils.passwort))
        except ValueError:
            raise LoginException

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
                                if fileName.lower().endswith('.doc') or fileName.lower().endswith('.docx'):
                                    print("Eine Word-Datei wurde geändert !")

                                print("Datei: " + fileName + " wurde geändert !\n")

    def countFiles(self):
        count2 = 0
        web_title = self.getWebTitle()
        for i in web_title:
            count2 += 1
            if self.__count < count2:
                print("Neue Datei hinzugekommen !!")
                self.__count = count2
                break

        return self.__count

    def init(self):
        print("Start init:")
        web_title = self.getWebTitle()
        for i in web_title:
            self.__count += 1
            for attribute, value in i.items():
                if attribute == 'TimeLastModified':
                    if self.__timeStamp < value:
                        self.__timeStamp = value

        print("Anzahl an Dateien:", self.__count)
